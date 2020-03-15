import Trigger
import discord

class Module:
    mode = "" # 0 for message / 1 for schedule / 2 for join
    name = ""
    Triggers = []
    Actions = []

    def __init__(self, name, mode):
        self.name = name
        self.mode = mode

    def addTrigger(self, trigger):
        self.Triggers.append(trigger)

    def removeTrigger(self, trigger):
        self.Triggers.remove(trigger)
        
    def addAction(self, action):
        self.Actions.append(action)

    def getName(self):
        return self.name
    
    def getMode(self):
        return self.mode
    
    def CheckTriggers(self, message):
        
        for x in self.Triggers:
            print(x.name)
            if x.checkState(message) == False:
                return False
        return True

#asyncio.run_coroutine_threadsafe()
