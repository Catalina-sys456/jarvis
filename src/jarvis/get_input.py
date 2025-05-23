import argparse
from jarvis.read_config import open_file

def get_args(provider, model):
    command_or_not = False
    provider = provider
    model = model
    message = ''
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file_name", type = str, help = "send a file to llm")
    parser.add_argument("-q", "--question", type = str, help = "ask llm a question")
    parser.add_argument("-p", "--provider", type = str, help = "change the provider")
    parser.add_argument("-m", "--model", type = str, help = "change a model")
    parser.add_argument("-c", "--command", type =str, help = "let llm gennerate commands")
    args = parser.parse_args()
    if args.model:
        model = args.model
    if args.command:
        command_or_not = True
        message = args.command
    elif args.file_name:   
        message = open_file(args.file_name)
    elif args.question:
        message = args.question
    return provider, model, message, command_or_not
