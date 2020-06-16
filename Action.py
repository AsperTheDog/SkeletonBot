import discord

class Action:
    type = 0
    args = []
    module = ""

    def __init__(self, module, args):
        self.module = module
        self.args = args

    def execute(self, arg):
        if type == 0:
            executeMessage(arg)
        elif type == 1:
            executeSchedule(arg)
        elif type == 2:
            executeJoin(arg)

    def executeMessage(self, arg):
        pass

    def executeSchedule(self, arg):
        pass

    def executeJoin(self, arg):
        pass

    def print(self, level):
        return "**" + self.name + "**: Pass"
