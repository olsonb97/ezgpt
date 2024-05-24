from ezgpt import EZGPT

gpt = EZGPT(temperature=1.0, commands=True)

while True:
    user_message = input("You: ")
    if cmd := gpt.send_msg(user_message):
        print(cmd)
        continue
    gpt_message = gpt.get_msg()
    print("GPT:", gpt_message)