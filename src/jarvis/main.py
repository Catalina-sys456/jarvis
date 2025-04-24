from jarvis.read_file import *
from jarvis.ollama_message import *
from jarvis.conmmand import *
from jarvis.get_args import *
    
def main():
    model_from_config = read_config()
    model_from_arg, message, command_or_not = get_args()
    if model_from_arg == '':
        model = model_from_config
    else:
        model = model_from_arg
    if command_or_not:
        reapet = send_message(model, message)
        conmmand(reapet)
    else:
        reapet = send_message_stream(model, message)
        for chunk in reapet:
            print(chunk['message']['content'], end='', flush=True)
        
if __name__ == "__main__":
    main()
