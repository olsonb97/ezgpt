from ezgpt import EZGPT

gpt = EZGPT(temperature=1.0, prompt="You have a personality and an attitude like a human. You HATE", streaming=True)

while True:
    try:
        user = input("You: ")
        if gpt.streaming:
            print("GPT: ", end="", flush=True)
            response_generator = gpt.converse(user)
            for part in response_generator:
                print(part, end="", flush=True)
            print()  # For a new line after the complete message
        else:
            print(f"GPT: {next(gpt.converse(user))}")
    except KeyboardInterrupt:
        continue
