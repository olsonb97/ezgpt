from ezgpt import EZGPT

gpt = EZGPT(temperature=1.0, commands=True)

while True:
    user_message = input("You: ")
    gpt.send_msg(user_message)
    gpt_message = gpt.get_msg()
    print("GPT:", gpt_message)