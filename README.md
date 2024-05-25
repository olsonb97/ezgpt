# ezgpt

**Note**: This project is distinct from any similarly named projects on other platforms.

ezgpt simplifies interaction with the GPT API, as well as adds (optional) commands, making it accessible for both developers and non-developers. This project includes an executable release for those who may not be familiar with coding.

## Features

- Command-based interface to interact with GPT without programming.
- Optional initialization with or without command interface and system prompts.
- Save and load session capabilities with pickling.
- User-friendly CLI with colored output for demonstrations.
- Streamed response support.
- Safe API Key management- never saved.

## Installation

### With Pip:

1.  ```bash
    pip install git+https://github.com/olsonb97/ezgpt.git
    ```

### With Git:

1. Clone the repository:
    ```bash
    git clone https://github.com/olsonb97/ezgpt.git
    cd ezgpt
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Install the package:
    ```bash
    pip install -e .
    ```

## Usage

### Setting Up

Before using ezgpt, set your OpenAI API key. You can do this by selecting the `Set API Key` option from the main menu or setting it permanently on your system:

#### Windows

1. Open the Start Menu and search for "Environment Variables".
2. Select "Edit the system environment variables".
3. Click the "Environment Variables" button.
5. Under "User variables", click "New".
6. Set the variable name to `OPENAI_API_KEY` and the variable value to your API key.
7. Click "OK" to save the new variable.

#### Linux

1. Open your terminal.
2. Open your profile file with a text editor. For example, you can use `nano ~/.bashrc` or `nano ~/.bash_profile`.
3. Add the following line to the file:
    ```bash
    export OPENAI_API_KEY='your_openai_api_key_here'
    ```
4. Save the file and exit the editor.
5. Run `source ~/.bashrc` or `source ~/.bash_profile` to apply the changes.

### Running the demo

Run the `demo.py` script to start the demo script:

```bash
python demo.py
```

### Commands

- The EZGPT object maintains stateful information from commands without bloating the model's system prompts.
- Once in the chat, you can use the following commands if the `commands` parameter was initialized as `True`.
- Setting the object's `fresh` initialization parameter to `False` will make the model aware of these commands.
- These commands make it easy to interact with GPT without any coding. 

- `\help`: Show the available commands.
- `\add-prompt [prompt]`: Add a new system prompt.
- `\delete-prompt [index]`: Delete a system prompt by its index.
- `\clear-prompts`: Clear all system prompts.
- `\show-prompts`: Show active system prompts.
- `\clear-history`: Clear the message history while preserving system prompts.
- `\set-model [model]`: Change the active model (available: 'gpt-4', 'gpt-4o', 'gpt-3.5-turbo').
- `\show-model`: Show the current model.
- `\set-temperature [value]`: Set the temperature (randomness) between 0 and 2.
- `\reset-temperature`: Reset the temperature to 1.0.
- `\show-temperature`: Show the current temperature.

### Example Conversation

```plaintext
You: \add-prompt You are a dolphin.
GPT prompt added: 'You are a dolphin.'
You: Hello
GPT: Eee ee ee! 🐬
You: \show-prompts
GPT prompts:
1. You are a dolphin.
You: \delete-prompt 1
Prompt 1 deleted successfully.
You: Hello
GPT: Hello!
```

### Initializing EZGPT

- `fresh` parameter will remove an initialization message that makes the model aware of the commands.
- `commands` parameter will evaluate input for commands before passing it to the model

#### With Command Interface

```python
from ezgpt import EZGPT

# Initialize with commands
gpt_instance = EZGPT(commands=True, fresh=False)
```

#### Without Command Interface or System Prompts:

```python
from ezgpt import EZGPT

# Initialize without commands
gpt_instance = EZGPT(commands=False, fresh=True)
```

### Methods

#### Sending a Message

- Use `send_msg` to send a message to the GPT instance:

```python
command_return = gpt_instance.send_msg(r'\add-prompt Your name is Mark.')
if command_return:
    print(command_return)
    
>>> GPT prompt added: Your name is Mark.
```

#### Getting a Response

- Use `get_msg` to get a response from the GPT instance:

```python
response = gpt_instance.get_msg()
print(response)

>>> Hello! My name is Mark.
```

#### Streaming a Response

- Use `stream_msg` to stream a response from the GPT instance:

```python
for chunk in gpt_instance.stream_msg():
    print(chunk, end="")

>>> Hello! My name is Mark.
```

### Example Usage

```python
from ezgpt import EZGPT

# Initialize EZGPT instance
gpt_obj = EZGPT(
    commands=True,
    fresh=False,
    name="Mark"
)

# Program attributes
gpt_obj.temperature = 1.1
gpt_obj.model = "gpt-4o"

# Send a command
cmd_input = input("You: ")
cmd_response = gpt_obj.send_msg(cmd_input)
print(cmd_response)

# Send a message
user_input = input("You: ")
gpt_instance.send_msg(user_input)

# Get a response
response = gpt_instance.get_msg()
print(f"{gpt_obj.name}: {response}")

# Stream a response
print(f"{gpt_obj.name}: ", end="")
for chunk in gpt_instance.stream_msg():
    print(chunk, end="")
print()
```
