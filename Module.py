import enum

class ModType(enum.Enum):
    message = 0
    schedule = 1
    join = 2


class Module:
    mode = 0
    name = ""
    Triggers = []
    Actions = []

    def __init__(self, name, mode):
        self.name = name
        self.mode = mode

    def addTrigger(self, trigger):
        self.Triggers.append(trigger)

    def addAction(self, action):
        self.Actions.append(action)

    def getName(self):
        return self.name
    
    def getMode(self):
        return self.mode