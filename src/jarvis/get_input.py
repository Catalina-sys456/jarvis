import argparse
from openai.types import image
import yaml
import os

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file_name", type = str, help = "send a file to llm")
    parser.add_argument("-q", "--question", type = str, help = "ask llm a question")
    parser.add_argument("-p", "--provider", type = str, help = "change the provider")
    parser.add_argument("-m", "--model", type = str, help = "change a model")
    parser.add_argument("-c", "--command", type =str, help = "let llm gennerate commands")
    parser.add_argument("-i", "--image", type=str, help = "generate image")
    args = parser.parse_args()
    return args.file_name, args.question, args.provider, args.model, args.command, args.image

def read_config():
    config_file = os.path.join(os.path.expanduser('~'), '.config/jarvis', 'config.yaml')
    try:
        with open(config_file) as file:
            configration = yaml.safe_load(file)
            provider = configration['provider']
            api_key = configration['api_key']
            model = configration['model']
            return provider, model, api_key
    except:
        print('failed to read the config file, does ~/.config/jarvis/config.yaml exist?')
        exit(0)

def get_input():
    '''
    Combine the values ​​obtained from x and y
    '''
    provider, model, api_key = read_config()
    args_filename, args_question, args_provider, args_model, args_command, args_image = get_args()
    command_or_not = False
    image_or_not = False
    message = ''
    if args_filename != None:
        with open (args_filename) as file:
            message = file
    elif args_question != None:
        message = args_question
    elif args_command != None:
        message = args_command
        command_or_not = True
    elif args_image != None:
        message = args_image
        image_or_not = True
    if args_provider != None:
        provider = args_provider
    if args_model != None:
        model = args_model
    return provider, model, api_key, message, command_or_not, image_or_not
