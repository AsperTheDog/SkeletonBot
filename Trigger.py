import enum
import discord

class TriggerType(enum.Enum):
    MessageContent = 0
    UserName = 1

class Trigger:
    mode = 0
    name = ""
    args = []
    def __init__(self, name, mode, args):
        self.mode = mode
        self.name = name
        self.args = args

    def checkState(self, message):
        if(self.mode == 0):
            print(self.mode)
            return self.checkMessageContent(message.content)
        elif(self.mode == 1):
            return self.checkUserName(message)
        else:
            return False
            
    def checkMessageContent(self, message):
        print(message + "\t\t" + self.args[0] + "\t\t" + self.args[1])
        if self.args[1] == "anywhere":  
            if message.find(self.args[0]) != -1:
                return True
        elif self.args[1] == "beginning":
            if message.find(self.args[0]) == 0:
                return True
        elif self.args[1] == "command":
            if message == args[0]:
                return True
        return False

        
    def checkUserName(self, message):
        return True
    
    def __str__(self):
        if self.mode == 0:
            return printMessageContent()
        if self.mode == 1:
            return printUserName()

    def printMessageContent(self):
        if self.args[1] == "anywhere":
            return "**" + self.name + "**: Checks if the text '" + self.args[0] + "' is contained in the message"
        elif self.args[1] == "beginning":
            return "**" + self.name + "**: Checks if the text '" + self.args[0] + "' is contained at the beginning of the message"
        elif self.args[1] == "command":
            return "**" + self.name + "**: Checks if the text '" + self.args[0] + "' is sent"
        
    def printUserName(self):
        return "**" + self.name + "**: Checks if the user " + self.args[0] + " is the person who sent the message"
