# llm-cli
This project allows you to access LLMs right from your terminal, CLI or shell, whatever you want to call it.  
The LLM can be local hosted or it can be any other LLM server that is OpenAI API compatible.  
Optimized for both local and server.  
The only requirement for the application to work is to have a working server that is OpenAI API compatible.  
This project is absolutely cross-platform and can run either via python interpreter or packed into an application (See more: [Usage](#usage)).  
I only tested it with [llama.cpp](https://github.com/ggml-org/llama.cpp) yet, because I dont have an OpenAI API key.  

# Features
* Get responses straight from the shell, terminal or CLI, whatever the name is.
* Feed the LLM with contents of files or even directories, following can be used, | pipe, $() syntax or a -w flag (--help will help).  
* [Installation](#installation) requires absolutely no graphical interface.
* Manipulate the history of conversations any way you want (--help will help).
* Ask LLM to execute commands for you with the knowledge of the OS running.
* Cross-platform as long as [python](https://www.python.org/) is.

# Installation
It can be done either by downloading a release or fully in CLI.  
## CLI installation
### Prerequisites
* [git](https://git-scm.com/)
* [python](https://www.python.org/)
* pip, comes with python
* (Optional) python-venv, comes with python

### Without venv:
#### Cross platform way:
```sh
git clone https://github.com/debugkei/llm-cli
cd llm-cli
pip install -r requirements.txt
```
### With venv:
#### Linux:
```sh
git clone `https://github.com/debugkei/llm-cli`  
cd llm-cli  
python -m venv  
source venv/bin/activate  
pip install -r requirements.txt  
```
#### Windows:
```sh
git clone `https://github.com/debugkei/llm-cli`  
cd llm-cli  
python -m venv  
venv\Scripts\activate  
pip install -r requirements.txt  
```

# Usage
```sh
python src/llm-cli.py -p your prompt
```
`-m` - name of the model on the server, if not specified uses `default`.  
`-u` - url of the server, if not specified uses `http://localhost:8080`.  
`-w` - paths for LLM to consider and read.  
`-r` - If provided with directories then read all files inside recursively, if flag isnt set then dont read recursively.  
`-e` - Exclude specific paths that LLM is not going to consider.  
`-t` - set the temperature for the LLM. Range 0-1, where 0 - be straight forward.  
`-a` - API, can be either specified, if not uses enviroment variable `OPENAI_API_KEY`, else assumed that API is not needed (running locally).  
  If API is not needed but envoriment variable has to stay, then use `-a not-needed`.  
`-h` - print out possible flags with their description.  
`-n` - disables history just for one message and turns it back on after.  
`-c` - clears the history.  
`-l` - specifies the length of history remembered, default is 3 previous conversations.  
`-s` - asks the LLM to execute commands in right in CLI for you, not recommended to use with LLMs that have below 7b parameters, they may output wrong format.  
`-d` - overrides the path to directory with history file, unrecommended to change unless making custom project structure.  
`-f` - limits the history that is serialized, with this flag the file contents given to LLM isnt saved to the history.  

Some CLIs dont allow special characters such as `()`, if so then just wrap the prompt into `""`.  

## Usage example with llama.cpp
1. Download precompiled binary from [here](https://github.com/ggml-org/llama.cpp/releases) for your platform and GPU rendering API.  
  Or to download via terminal:
  ```sh
  git clone https://github.com/ggml-org/llama.cpp
  ```
  And then build it, how to build is [here](https://github.com/ggml-org/llama.cpp#building-the-project)  
2. Download a model from [here](https://huggingface.co/) or to download via CLI [stackoverflow discussion](https://stackoverflow.com/questions/67595500/how-to-download-a-model-from-huggingface)  
3. Start the server:  
```sh
cd to/your/llama.cpp/installation  
./llama-server -m /path/to/your/model.gguf -c 2048 -ngl 200  
```
`-ngl` - amount of work offloaded to gpu, everything above 100 is 100, and if you planning on using CPU, then just dont include -ngl.  
`-c` - context, for bigger prompts, files or directories use greater values.  
4. [Usage](#usage)  
  * Not need to specify the URL because default URL of ./llama-server is `http://localhost:8080`.  
  * If multimodel server then in [usage](#usage) specify the model, else if only 1 model is hosted then default will handle the job.
  * API is not needed so just dont set the flag

# Development
* The pull requests with a lot of changes will not be accepted, thats my own project for now.
## Roadmap/TODO
* Feeding of files to LLM (Done)
* Executing commands from LLM (Done)
* Releases and packaged application via [pyinstaller](https://github.com/pyinstaller/pyinstaller), or alias use with python
* Add usage examples images in README.md, maybe additionally add github actions.
* Ask LLM to modify files.
* Image generation/describing???
* Get HTML contents of webpages, transcripts of [Youtube](https://www.youtube.com/) videos, [llm-axe](https://github.com/emirsahin1/llm-axe) can be helpful.
## Branches
* dev is for adding new features.
* main is for keeping all the main files, dev is merged with it.
* Each release branch will be created.

# Dependencies
## To install all
```sh
pip install -r requirements.txt  
```
## List
* openai (python package)
* os (python package, builtin)
* pathlib (python package, builtin)
* argparse (python package, builtin)
* platform (python package, builtin)
* sys (python package, builtin)
* subprocess (python package, builtin)
