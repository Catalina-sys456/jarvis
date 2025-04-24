from ollama import chat
from ollama import ChatResponse

def send_message(a, b):
    """
    get string from ollama
    """
    response: ChatResponse = chat(model= a, messages=[
  {
    'role': 'user',
    'content': b,
  },
])
    repeat = response['message']['content']
    return repeat

def send_message_stream(a, b):
    """
    get string stream from ollama
    """
    stream = chat(
      model= a,
      messages=[{'role': 'user', 'content': b}],
      stream=True,
      )
    return stream
