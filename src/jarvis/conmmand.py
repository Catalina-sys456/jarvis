from os import system
from re import findall
def conmmand(stream):
    """
    cut the string sent from the server.
    most conmmand are preceded by $ or between ```  ```
    """
    if "$" in stream:
        cutted_command = '\n'.join(findall(r"\$(.*?)\n", stream))
    else:
        cutted_command = '\n'.join(findall(r"\`(.*?)\`", stream))
    print(cutted_command)
    y_or_not = input("[y/n/show]")
    if y_or_not == 'y':
        system(cutted_command)
    elif y_or_not == 'show':
        print(stream)
    else:
        print("type your conmmand")
