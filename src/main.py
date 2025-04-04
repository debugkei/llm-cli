from argparser import GetArgs
import paths
import os
import platform
import history
import llmserver
import llmsystemprompts
import commandshandler
import datetime

# Get the args parsed
args = GetArgs()

# Init the server
llmserver.Init(args.url, args.api or os.getenv("OPENAI_API_KEY") or "not-needed")

# Add the system prompt
requirements = llmsystemprompts.GetDefault()

if args.shell:
  requirements += llmsystemprompts.GetShell()

if args.code:
  requirements += llmsystemprompts.GetCode()

llmserver.AddSystemPropmt(requirements)

# Get client's prompt
prompt = " ".join(args.prompt or '') # This syntax because user isnt always wrapping prompt into "", it may turn out to be separated by spaces

# Set history file location
history.historyFilePath = args.cache_location or paths.GetCacheDir("llm-cli")/"history"

# Set history length
historyLength = args.history_length * 2 if args.history_length >= 0 else 0 # Handle possible negative input
history.historyLimit = historyLength # * 2 because prompt and output are saved

# If clear history flag is on
if args.history_clear:
  history.ClearHistory() # TODO: if prompt is empty then exit
  if len(prompt) == 0:
    exit(0)
elif not args.no_history: # Pull out previous responses from the history and feed them along with current ones, if history is enabled
  historyEntries = history.Deserialize()
  i = 0
  while i < len(historyEntries):
    llmserver.AddUserPropmt(historyEntries[i])
    i += 1
    llmserver.AddAssistantPropmt(historyEntries[i])
    i += 1
  
# Create full prompt
fullPrompt = f"""\
Contents: {args.pipe}\n\
{paths.GetPathsContents(args.path, args.exclude, args.recursive)}\n\
My Prompt: {prompt}
"""

# Inform LLM about current contents, user prompt, CWD, system and release.
llmserver.AddUserPropmt(f"""\
{fullPrompt}\n\
CWD: {os.getcwd()}\n\
System: {platform.system()}\n\
Release: {platform.release()}\n\
Current time: {datetime.datetime.now()}
""")
# Escape characters are added for proper formatting

def main():
  # Generate and print stream output
  temperature = args.temperature if args.temperature >= 0 else 0
  output = llmserver.PrintRespond(model=args.model, temperature=temperature, isStreaming=True, doIgnoreTripleBacktick=args.code and not args.shell)

  # Save the response and prompt to history, only if history is enabled
  if not args.no_history: # If saving to history
    if args.limit_history: # If limit history, dont save contents
      history.Serialize(prompt) # Serialize only the prompt
    else:
      history.Serialize(fullPrompt) # Else serialize the contents also

    history.Serialize(output)

  # If commands were asked to execute
  if args.shell:
    commands = []
    parsingCommands = False
    for line in output.splitlines(): # Parse commands into a list
      # Only parse commands within ```sh ``` syntax
      if line.startswith("```"):
        parsingCommands = not parsingCommands
        continue

      # Only parse when necessary
      if parsingCommands:
        commands.append(line)

    # If commands are empty, no commands were found
    if len(commands) == 0:
      exit(0)

    # Clear prompt about format and give the LLM its output
    llmserver.ClearSystemPrompts()
    llmserver.AddSystemPropmt(llmsystemprompts.GetDefault())
    llmserver.AddAssistantPropmt(output)
      
    # Ask and execute the commands
    commandshandler.PromptUserAndExecute(commands, model=args.model, temperature=temperature)

# Call main
if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    print(f"\nKeyboardInterrupt")
