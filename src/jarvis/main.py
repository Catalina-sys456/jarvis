from jarvis.read_config import *
from jarvis.llm_client import *
from jarvis.conmmand import *
from jarvis.get_input import *

def llm_chat(provider, model, api_key):
    while  True:
        try:
            message = input('\n\n\n>>> ')
            reapet_stream = llm_client(provider, model, api_key, message)
            reapet_stream.generate_stream_print()
        except EOFError:
            break
            
def main():
    provider, model, api_key = read_config()
    model, message, command_or_not = get_args(provider, model)
    if command_or_not:
        reapet = llm_client(provider,  model, api_key, message)
        reapet = reapet.generate()
        conmmand(reapet)
    elif message != '':
        reapet_stream = llm_client(provider, model, api_key, message)
        reapet_stream.generate_stream_print()
    else:
        llm_chat(provider, model, api_key)
