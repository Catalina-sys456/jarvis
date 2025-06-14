from sys import exit
from litellm import completion, image_generation

class llm_client:
    def __init__(self, provider, model, api_key, message):
        self.provider = provider.lower()
        self.model = model.lower()
        self.api_key = api_key
        self.message = message

    def llm_generate(self):
        try:
            response = completion(
                api_key = self.api_key,
                model = f'{self.provider}/{self.model}',
                messages = [{ "content": self.message,"role": "user"}],
            )
            return response.choices[0].message.content
        except:
            print(f'failed to get the answer from {self.provider}')
            exit(1)
            
    def llm_generate_stream(self):
        try:
            response = completion(
                api_key = self.api_key,
                model = f'{self.provider}/{self.model}',
                messages = [{ "content": self.message,"role": "user"}],
                stream=True,
            )
            return response
        except:
            print(f'failed to get answer from {self.provider}')
            exit(1)

    def generate_stream_print(self):
        reponse = self.llm_generate_stream()
        for chunk in reponse:
            print(chunk.choices[0].delta.content, end="", flush=True)

    def llm_chat(self):
        while  True:
            try:
                print('-' * 60)
                self.message = input('>>> ')
                print('-' * 60)
                self.generate_stream_print()
            except EOFError:
                break

    def generate_image(self):
        try:
            response = image_generation(
                api_key = self.api_key,
                model = f'{self.provider}/{self.model}',
                prompt = f'{self.message}'
            )
            print(f"response: {response}")
        except:
            print(f'failed to get the answer from {self.provider}')
            exit(1)        
        
