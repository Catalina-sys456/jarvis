* jsrvis, a cli llm client

** usage:

	usage: jarvis [-h] [-f FILE_NAME] [-q QUESTION] [-p PROVIDER] [-m MODEL] [-c COMMAND]

	options:
	-h, --help            show this help message and exit
	-f FILE_NAME, --file_name FILE_NAME
                        send a file to llm
	-q QUESTION, --question QUESTION
                        ask llm a question
	-p PROVIDER, --provider PROVIDER
                        change the provider
	-m MODEL, --model MODEL
                        change a model
	-c COMMAND, --command COMMAND
                        let llm gennerate commands
** configration:
  
move config.yaml to ~/.config/jarvis/config.yaml
