
# ezgpt

ezgpt simplifies interaction with the GPT API, making it accessible for both developers and non-developers. This project includes an executable release for those who may not be familiar with coding.

## Features

- Command-based interface for non-coders to interact with GPT without programming.
- Optional initialization with or without command interface and system prompts.
- Save and load session capabilities.
- User-friendly CLI with colored output for demonstrations.
- Streamed response support.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/ezgpt.git
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

Before using ezgpt, set your OpenAI API key. You can do this by selecting the `Set API Key` option from the main menu or setting it directly in your environment:

#### Bash
```bash
export OPENAI_API_KEY='your-api-key'
```

#### Windows Command Prompt
```cmd
set OPENAI_API_KEY='your-api-key'
```

### Running the demo

Run the `demo.py` script to start the application:

```bash
python demo.py
```

### Commands

Once in the chat, you can use the following commands if the cmd_bool parameter was initialized as `True`. These commands make it easy to interact with GPT without any coding. The EZGPT object maintains stateful information about these interactions:

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
You: EEeee!
GPT: Ee-ee-ee! 🐬💦
```

### Initializing EZGPT

#### With Command Interface
- `fresh` parameter will remove an initialization message that makes the model aware of the commands.
- `commands` parameter will evaluate input for commands before passing it to the model


```python
from ezgpt import EZGPT

# Initialize with commands
gpt_instance = EZGPT(commands=True, fresh=False)
```

#### Without Command Interface

- To initialize a blank GPT instance without commands or system prompts:

```python
from ezgpt import EZGPT

# Initialize without commands
gpt_instance = EZGPT(commands=False, fresh=True)
```

### Methods

#### Sending a Message

- Use the `send_msg` method to send a message to the GPT instance:

```python
command_return = gpt_instance.send_msg("Hello, GPT!")
if command_return:
    print(command_return)
    
GPT prompt added: You are a dolphin.
```

#### Getting a Response

- Use the `get_msg` method to get a response from the GPT instance:

```python
response = gpt_instance.get_msg()
print(response)
```

#### Streaming a Response

- Use the `stream_msg` method to stream a response from the GPT instance:

```python
for chunk in gpt_instance.stream_msg():
    print(chunk, end="")
```

### Example Usage

```python
from ezgpt import EZGPT

# Initialize EZGPT instance
gpt_instance = EZGPT(commands=True, fresh=False)
gpt_name = gpt_instance.name

# Program attributes
gpt_instance.temperature = 1.1
gpt_instance.model = "gpt-4"

# Send a command
cmd_input = input("You: ")
cmd_response = gpt_instance.send_msg(cmd_input)
print(cmd_response)

# Send a message
user_input = input("You: ")
gpt_instance.send_msg("Hello, GPT-Dolphin!")

# Get a response
response = gpt_instance.get_msg()
print(f"{gpt_name}: {response}")

# Stream a response
print(f"{gpt_name}: ", end="")
for chunk in gpt_instance.stream_msg():
    print(chunk, end="")
```
