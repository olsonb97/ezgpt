cmd_dict = [
    {
        "description": "Help: show the available commands",
        "syntax": r"\help",
        "action": "_EZGPT__help_command",
        "params": False
    },
    {
        "description": "Add a Prompt: add a new prompt for system behavior by appending it to this command",
        "syntax": r"\add-prompt ",
        "action": "_EZGPT__add_prompt_command",
        "params": True
    },
    {
        "description": "Delete a Prompt: Delete a system prompt by appending it's index to this command (show-prompts to see indices)",
        "syntax": r"\delete-prompt ",
        "action": "_EZGPT__delete_prompt_command",
        "params": True
    },
    {
        "description": "Clear Prompts: remove all system prompts",
        "syntax": r"\clear-prompts",
        "action": "_EZGPT__clear_prompts_command",
        "params": False
    },
    {
        "description": "Show Prompts: show active system prompts",
        "syntax": r"\show-prompts",
        "action": "_EZGPT__show_prompts_command",
        "params": False
    },
    {
        "description": "Clear Screen: clear all messages from the screen",
        "syntax": r"\clear-screen",
        "action": "_EZGPT__clear_screen_command",
        "params": False
    },
    {
        "description": "Clear History: reset the message history; preserves system prompts",
        "syntax": r"\clear-history",
        "action": "_EZGPT__clear_history_command",
        "params": False
    },
    {
        "description": f"Set Model: change the active model by appending the model-name to this command",
        "syntax": r"\set-model ",
        "action": "_EZGPT__set_model_command",
        "params": True
    },
    {
        "description": "Show Model: show the active model",
        "syntax": r"\show-model",
        "action": "_EZGPT__show_model_command",
        "params": False
    },
    {
        "description": "Set Temperature: sets the randomness between 0-2, with 0 being deterministic and 2 random.",
        "syntax": r"\set-temperature ",
        "action": "_EZGPT__set_temperature_command",
        "params": True
    },
    {
        "description": "Reset Temperature: resets the randomness to 1.0",
        "syntax": r"\reset-temperature",
        "action": "_EZGPT__reset_temperature_command",
        "params": False
    },
    {
        "description": "Show Temperature: displays the current temperature",
        "syntax": r"\show-temperature",
        "action": "_EZGPT__show_temperature_command",
        "params": False
    },
    {
        "description": "Set Name: set the name for the assistant by appending the name to this command",
        "syntax": r"\set-name ",
        "action": "_EZGPT__set_name_command",
        "params": True
    },
    {
        "description": "Reset Name: reset the name of the system",
        "syntax": r"\reset-name",
        "action": "_EZGPT__reset_name_command",
        "params": False
    },
]