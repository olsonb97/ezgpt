from ezgpt import EZGPT

gpt = EZGPT(temperature=1.0, commands=True)

def manual_convo():
    while True:
        user_message = input("You: ")
        if cmd_return := gpt.send_msg(user_message):
            print(cmd_return)
            continue
        gpt_message = gpt.get_msg()
        print("GPT:", gpt_message)

def manual_stream():
    while True:
        user_message = input("You: ")
        if cmd_return := gpt.send_msg(user_message):
            print(cmd_return)
            continue
        print("GPT: ", end="", flush=True)
        for chunk in gpt.stream_msg():
            print(chunk, end="", flush=True)
        print()

def auto_convo():
    gpt.conversation(stream=True, color=False)

auto_convo()
# manual_convo()
# manual_stream()