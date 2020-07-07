import enum
import discord
import utility

class TriggerType(enum.Enum):
    MessageContent = 0
    UserName = 1

class Trigger:
    def __init__(self, name, mode, module, args):
        self.mode = mode
        self.name = name
        self.args = args
        self.module = module

    def checkState(self, message):
        if self.module.mode == utility.getModType("message"):
            if(self.mode == 0):
                return self.checkMessageContent(message.content)
            elif(self.mode == 1):
                return self.checkUserName(message)
            elif(self.mode == 2):
                return self.checkVariable()
            elif(self.mode == 3):
                return self.checkCommand()
            else:
                return False
        return False

    def checkMessageContent(self, message):
        if self.args[1] == "anywhere":
            if message.find(self.args[0]) != -1:
                return True
        elif self.args[1] == "beginning":
            if message.find(self.args[0]) == 0:
                return True
        elif self.args[1] == "command":
            if message == self.args[0]:
                return True
        return False

    def checkUserName(self, message):
        if message.author.name == args[0]:
            return True
        return False

    def print(self):
        if self.mode == 0:
            return self.printMessageContent()
        elif self.mode == 1:
            return self.printUserName()
        else:
            return str(self.mode)

    def checkVariable(self):
        for x in self.module.variables:
            if x == self.args[0]:
                return module.variables.get(x) == args[1]
        return False

    def processCommand(self, command):
        args = []
        

    def printMessageContent(self):
        if self.args[1] == "anywhere":
            return "**" + self.name + "**: Checks if the text '" + self.args[0] + "' is contained in the message"
        elif self.args[1] == "beginning":
            return "**" + self.name + "**: Checks if the text '" + self.args[0] + "' is contained at the beginning of the message"
        elif self.args[1] == "command":
            return "**" + self.name + "**: Checks if the text '" + self.args[0] + "' is sent"
        
    def printUserName(self):
        return "**" + self.name + "**: Checks if the user " + self.args[0] + " is the person who sent the message"
