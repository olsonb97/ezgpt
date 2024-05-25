from ezgpt import EZGPT

model = EZGPT(
    model = 'gpt-4o',
    name = 'GPT',
    commands = True
)

model.conversation(
    color = True,
    stream = True
)