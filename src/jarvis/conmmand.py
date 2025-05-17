from os import system
from re import findall

def cut_command(llm_feedback):
    cuttied_conmmand = '\n'
    if 'bash' in llm_feedback:
        cuttied_conmmand = findall(r"bash\n(.*?)\n", llm_feedback)
        return cuttied_conmmand
    if '$' in llm_feedback:
        cuttied_conmmand = findall(r"\$\n(.*?)\n", llm_feedback)
        return cuttied_conmmand
    if '```' in llm_feedback:
        cuttied_conmmand = findall(r"\`\`\`\n(.*?)\n", llm_feedback)
        return cuttied_conmmand
    else:
        return cuttied_conmmand

def conmmand(llm_feedback):
    cutted_command = cut_command(llm_feedback)
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
