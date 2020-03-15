import enum

class TriggerType(enum.Enum):
    MessageContent = 0
    PlayerName = 1


class Trigger:
    type = 0
    triggered = False
    name = ""
    def __init__(self, name, mode):
        self.mode = mode
        self.name = name

    def checkState(self):
        return self.triggered
