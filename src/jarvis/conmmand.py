from os import system
from re import findall

def conmmand(llm_feedback):
    print(llm_feedback)
    cutted_command = '\n'
    if '$' in llm_feedback:
        cutted_command = findall(r"\$(.*?)\n", llm_feedback)
    elif '`' in llm_feedback:
        cutted_command = findall(r"```\n(.*?)\n```", llm_feedback)
    else:
        cutted_command = findall(r"bash\n(.*?)\n```", llm_feedback)
    print(cutted_command)
    for line in cutted_command:
        print(f'\n{line}')
        action = input('Implement the conmmand or show the entire text? [y/n/show]')
        if action == 'y':
            system(line)
        elif action == 'show':
            print(llm_feedback)
            print(f"\n\n{line}")
            implement_or_not = input('Implement the conmmand? [y/n]')
            if implement_or_not == 'y':
                system(line)    

