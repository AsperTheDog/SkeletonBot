import Trigger
import discord

import utility

class Module:

    def __init__(self, name, mode):
        self.name = name
        self.mode = mode
        self.active = 0
        self.triggers = []
        self.actions = []
        self.variables = []


    def addTrigger(self, trigger):
        self.triggers.append(trigger)

    def removeTrigger(self, trigger):
        self.triggers.remove(trigger)
        
    def addAction(self, action):
        self.actions.append(action)

    def getName(self):
        return self.name
    
    def getMode(self):
        return self.mode
    
    def checkTriggers(self, message):
        
        for x in self.triggers:
            print(x.name)
            if x.checkState(message) == False:
                return False
        return True

    def execute(self, arg):
        if self.active == 1:
            if checkTriggers(arg) == True:
                executeActions(arg)

    def executeActions(self, arg):
        for x in actions:
            x.execute(arg)
    
    def print(self, level):
        string = ""
        string += "Module '**" + self.name + "**' of type '**" + utility.getModType(str(self.mode)) + "**'\n"
        for ts in range(level):
            string += "|\t\t"
        string += "**Triggers**\n"
        if len(self.triggers) == 0:
            for ts in range(level):
                string += "|\t\t"
            string += "\t\t"
            string += "There are no triggers (the module will always execute)\n"
        else:
            for x in self.triggers:
                for ts in range(level):
                    string += "|\t\t"
                string += "\t\t"
                string += str(x) + "\n"
        for ts in range(level):
            string += "|\t\t"
        string += "**Actions**\n"
        if len(self.actions) == 0:
            for ts in range(level):
                string += "|\t\t"
            string += "\t\t"
            string += "There are no actions (nothing will happen if it executes)\n"
        else:
            for x in self.actions:
                for ts in range(level):
                    string += "|\t\t"
                string += "\t\t"
                string += x.print(level + 1) + "\n"
        for ts in range(level):
            string += "|\t\t"
        string += "**Stored variables**\n"
        if len(self.variables) == 0:
            for ts in range(level):
                string += "|\t\t"
            string += "\t\t"
            string += "There are no variables"
        else:
            for x in self.variables:
                for ts in range(level):
                    string += "|\t\t"
                string += "\t\t"
                if x != self.variables[-1]:
                    string += str(x) + "\n"
                else:
                    string += str(x)
        return string

#asyncio.run_coroutine_threadsafe()
