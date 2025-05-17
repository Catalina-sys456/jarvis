from sys import exit
from ollama import chat
from ollama import ChatResponse
from google import genai

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
            print('failed to get the answer from ollama')
            exit(1)
    def __call_gemini(self):
        try:
            client = genai.Client(api_key=self.api_key)
            response = client.models.generate_content(
                model=self.model, contents=self.message
            )
            response = response.text
            return response
        except:
            print('failed to get the answer from gemini')
            exit(1)
            
    def __call_ollama_stream(self):
        try:
            stream = chat(
                model= self.model,
                messages=[{'role': 'user', 'content': self.message}],
                stream=True,
            )
            return stream
        except:
            print('failed to get answer from ollama')
            exit(1)

    def __call_gemini_stream(self):
        try:
            client = genai.Client(api_key=self.api_key)
            response = client.models.generate_content_stream(
                model=self.model,
                contents=[self.message]
                )
            return response
        except:
             print('failed to get the answer from gemini')
             exit(1)
             
            

    def generate(self):
        match self.provider.lower():
            case 'ollama':
                return self.__call_ollama()
            case 'gemini':
                return self.__call_gemini()
            case 'deepseek':
                return self.__call_deepseek()

    def generate_stream(self):
        match self.provider.lower():
            case 'ollama':
                return self.__call_ollama_stream()
            case 'gemini':
                return self.__call_gemini_stream()
            case 'deepseek':
                return self.__call_deepseek_stream()

    def generate_stream_print(self):
        match self.provider.lower():
            case 'ollama':
                reponse = self.__call_ollama_stream()
                for chunk in reponse:
                    print(chunk['message']['content'], end='', flush=True)
            case 'gemini':
                reponse = self.__call_gemini_stream()
                for chunk in reponse:
                    print(chunk.text, end="")
