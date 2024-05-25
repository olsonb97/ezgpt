from tkinter import filedialog, Tk
import pickle
import sys
import os
import colorama
from src.ezgpt import EZGPT

def print_system(message):
    print(f"{colorama.Fore.LIGHTMAGENTA_EX}{message}{colorama.Style.RESET_ALL}")

def save(ezgpt):
    root = Tk()
    root.withdraw()  # Hide the root window
    root.attributes('-topmost', True)
    filename = filedialog.asksaveasfilename(
        defaultextension=".pkl",
        filetypes=[("Pickle files", "*.pkl")],
        title="Save EZGPT"
    )
    if filename:
        with open(filename, 'wb') as f:
            pickle.dump(ezgpt, f)
        print_system(f"EZGPT saved to {filename}")

def load():
    root = Tk()
    root.withdraw()  # Hide the root window
    root.attributes('-topmost', True)
    filename = filedialog.askopenfilename(
        defaultextension=".pkl",
        filetypes=[("Pickle files", "*.pkl")],
        title="Load EZGPT"
    )
    if filename:
        with open(filename, 'rb') as f:
            return pickle.load(f)
    print_system("No file selected or loading failed.")
    return None

def main_menu():
    ezgpt = None
    while True:
        print_system("\nMain Menu:\n")
        print_system("    1. Chat")
        print_system("    2. Set API Key")
        print_system("    3. Load EZGPT")
        print_system("    4. Save EZGPT")
        print_system("    5. Exit\n")
        choice = input("Choose an option: ").strip()
        if choice == '1':
            if ezgpt is None:
                ezgpt = EZGPT(commands=True, fresh=False)
            enter_chat(ezgpt)
        elif choice == '2':
            set_api_key()
        elif choice == '3':
            ezgpt = load()
            if ezgpt:
                print_system("EZGPT loaded successfully.")
        elif choice == '4':
            if ezgpt:
                save(ezgpt)
            else:
                print_system("No active EZGPT instance to save.")
        elif choice == '5':
            sys.exit()
        else:
            print_system("\nInvalid choice. Please choose again.")

def set_api_key():
    try:
        api_key = input("Enter your OpenAI API Key: ").strip()
        if api_key:
            os.environ['OPENAI_API_KEY'] = api_key
            print_system("\nAPI Key set successfully.")
        else:
            print_system("\nAPI Key cannot be empty.")
    except KeyboardInterrupt:
        print_system("\nReturning to main menu...")
    except Exception as e:
        print_system(f"API Key error: {e}")

def enter_chat(ezgpt):
    try:
        ezgpt.conversation(stream=True, color=True)
    except KeyboardInterrupt:
        print_system("\nReturning to main menu...")
    except Exception as e:
        print_system(f"\nChat Error: {e}")

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print_system("\nProgram interrupted. Exiting...")
        sys.exit()