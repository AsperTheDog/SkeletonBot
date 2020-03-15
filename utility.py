from os import listdir
import Module

def SplitCommand(command):
    aux = command
    sp = aux.split('"')
    i = 0
    while ' ' in sp:
        sp.remove(' ')
    return sp

def LoadActiveModules():
    ActiveModules = []
    f = open("ModList.txt","r")
    ActiveModules = f.readlines()
    
    f.close()
    return ActiveModules

def LoadModules():
    i = 0
    Modules = []
    ActiveModules = LoadActiveModules()
    
    for x in listdir("Modules"):
        f = open("Modules\\" + x, "r")
        lines = f.readlines()
        for x in lines:
            if(x == ""): i+=1
            if(i==0):
                c = SplitCommand(x)
                if(c[0] not in ActiveModules):
                    break
                Modules.append(Module.Module(c[0],c[1]))
            #if(i==1):
                #check type
                #append triggers to module.
        f.close()
    return Modules

def RefreshModules(list):
    f = open("ModList.txt","w")
    for x in list:
        f.write(x + "\n")
    f.close()

def GetModType(str):
    if str == "m" or str == "message" or str == "0":
        return "message"
    if str == "s" or str == "schedule" or str == "1":
        return "schedule"
    if str == "j" or str == "join" or str == "2":
        return "join"

def PrintModules(list):
    for x in list:
        str += "Name: " + x.getName() + ", Mode: " + x.getMode() + "\n"
    return str
