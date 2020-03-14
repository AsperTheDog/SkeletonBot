
def SplitCommand(command):
    aux = command
    sp = aux.split('"')
    i = 0
    while ' ' in sp:
        sp.remove(' ')
    return sp

def LoadModules(path):
