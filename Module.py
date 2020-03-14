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

    def __init__(self, mode):
        self.mode = mode

    def addTrigger(trigger):
        Triggers.append(trigger)

    def addAction(action):
        Actions.append(action)
