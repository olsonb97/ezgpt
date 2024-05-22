import os
from openai import OpenAI

class EZGPT:
    def __init__(self, model: str = 'gpt-4o', prompt: str = "", temperature=1.0):
        self.model = model
        self.temperature = temperature
        self.initialize_client()
        self.messages = []
        if prompt:
            self.messages.append({"role": "system", "content": prompt})

    def initialize_client(self):
        self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    def send_message(self, user_input):
        self.messages.append({"role": "user", "content": user_input})
        return user_input
    
    def receive_streaming_message(self):
        pass

    def receive_non_streaming_message(self):
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.messages,
                temperature=self.temperature,
                stream=False
            )
            message = response.choices[0].message.content
            self.messages.append({"role": "assistant", "content": message})
            yield message
        except (IndexError, KeyError) as e:
            raise ValueError(f"Error extracting message from response: {e}")

    def converse(self, input, stream=False):
        self.send_message(input)
        if stream:
            return list(self.receive_streaming_message())
        else:
            return next(self.receive_non_streaming_message())

    def __getstate__(self):
        # Exclude the client
        state = self.__dict__.copy()
        state['client'] = None
        return state
    
    def __setstate__(self, state):
        # Initialize client
        self.__dict__.update(state)
        self.initialize_client()
