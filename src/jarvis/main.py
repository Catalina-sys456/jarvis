from jarvis.llm_client import *
from jarvis.command import *
from jarvis.get_input import *

def main():
    provider, model, api_key, message, command_or_not, image_or_not = get_input()
    if command_or_not:
        reapet = llm_client(provider,  model, api_key, message)
        reapet = reapet.llm_generate()
        command(reapet)
    elif image_or_not:
        reapet = llm_client(provider, model, api_key, message)
        reapet.generate_image
    elif message != '':
        reapet_stream = llm_client(provider, model, api_key, message)
        reapet_stream.generate_stream_print()
    else:
        reapet = llm_client(provider, model, api_key, message)
        reapet.llm_chat()
