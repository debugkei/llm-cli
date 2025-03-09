# llm-cli
This project allows CLI use of LLMs through any server that supports OpenAI API.  
I used the program with llama.cpp's server.  

# Features
* Get responses from terminal.
* Input files and whole directories into LLMs for them to read.
* Execute commands generated by LLMs right in the terminal

# Installation
## Without venv:
### Cross platform way:
```sh
git clone https://github.com/debugkei/llm-cli
cd llm-cli
pip install -r requirements.txt
```
## With venv:
### Linux:
```sh
git clone `https://github.com/debugkei/llm-cli`  
cd llm-cli  
python -m venv  
source venv/bin/activate  
pip install -r requirements.txt  
```
### Windows:
```sh
git clone `https://github.com/debugkei/llm-cli`  
cd llm-cli  
python -m venv  
venv\Scripts\activate  
pip install -r requirements.txt  
```

# Usage
```sh
python src/llm-cli.py your_API_URL your_model_name -f your/optional_file -d your/optional_dir your prompt  
```
If that's too long to type I recommend creating alias.  
Alias will bind the API_URL and model as arguments for llm-cli, and will allow use from anywhere.  
#### Linux bash:
```bash
echo 'alias llm-cli='python path/to/llm-cli.py your_API_URL your_model_name'' >> ~/.bashrc  
```

#### Linux zsh:
```zsh
echo 'alias llm-cli='python path/to/llm-cli.py your_API_URL your_model_name'' >> ~/.zshrc  
```

#### Windows powershell:
```powershell
Add-Content -Path $PROFILE -Value "function llm-cli { python path/to/llm-cli.py your_API_URL your_model_name }"  
```

## Usage example with llama.cpp
1. Download precompiled binary from [here](https://github.com/ggml-org/llama.cpp/releases) for your platform and GPU rendering API
2. Start the server:
```sh
cd to/your/llama.cpp/installation  
./llama-server -m /path/to/your/model -c 2048 -ngl 200  
```
-ngl is amount of work offloaded to gpu, everything above 100 is 100, and if you planning on using CPU, then just dont include -ngl.  
-c is context, for bigger prompts, files or directories use greater values.  
3. [Usage](#usage)
  * API_URL is http://localhost:8080
  * Model name is model file name without .gguf

# Dependencies
## To download all
```sh
pip install -r requirements.txt  
```
## List
* openai (python package)

# Development
### This project is actively developed right now.
* No releases.
* No pull requests will be accepted.
