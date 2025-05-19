from jarvis.read_config import *
from jarvis.llm_client import *
from jarvis.command import *
from jarvis.get_input import *

def main():
    provider, model, api_key = read_config()
    provider, model, message, command_or_not = get_args(provider, model)
    if command_or_not:
        reapet = llm_client(provider,  model, api_key, message)
        reapet = reapet.llm_generate()
        command(reapet)
    elif message != '':
        reapet_stream = llm_client(provider, model, api_key, message)
        reapet_stream.generate_stream_print()
    else:
        reapet = llm_client(provider, model, api_key, message)
        reapet.llm_chat()
