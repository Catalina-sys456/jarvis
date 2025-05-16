from ollama import chat
from ollama import ChatResponse

class llm_client:
    def __init__(self, provider, model, api_key, message):
        self.provider = provider
        self.model = model
        self.api_key = api_key
        self.message = message
    def __call_ollama(self):
        try:
            response: ChatResponse = chat(model= self.model, messages=[
                {
                    'role': 'user',
                    'content': self.message,
                },
            ])
            repeat = response['message']['content']
            return repeat
        except:
            print('failed to get the answer from llm')
    def __call_ollama_stream(self):
        try:
            stream = chat(
                model= self.model,
                messages=[{'role': 'user', 'content': self.message}],
                stream=True,
            )
            return stream
        except:
            print('failed to get answer from llm')

    def generate(self):
        if self.provider.lower() == 'ollama' :
            return self.__call_ollama()

    def generate_stream(self):
        if self.provider.lower() == 'ollama' :
            return self.__call_ollama_stream()            
