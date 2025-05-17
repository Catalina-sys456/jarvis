import argparse
from jarvis.read_config import open_file
def get_args(provider, model):
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file_name", type = str, help = "send a file to llm")
    parser.add_argument("-w", "--word", type = str, help = "ask llm a question")
    parser.add_argument("-p", "--provider", type = str, help = "change the provider")
    parser.add_argument("-m", "--model", type = str, help = "change a model")
    parser.add_argument("-c", "--conmmand", type =str, help = "let llm gennerate conmmands")
    args = parser.parse_args()
    command_or_not = False
    provider = provider
    model = model
    message = ''
    if args.model:
        model = args.model
    if args.conmmand:
        command_or_not = True
        message = args.conmmand
    elif args.file_name:   
        message = open_file(args.file_name)
    elif args.word:
        message = args.word
    return model, message, command_or_not
