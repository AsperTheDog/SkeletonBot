from src.Modules.action import ActionManager
from src.Modules.trigger import TriggerManager
from src.Modules.Triggers import *
from src.Modules.Actions import *


def deserialize(data, bot):
    mod = Module(data['name'], data['type'], data['activated'], data['variables'])
    for tr in data['triggers']:
        mod.addTrigger(tr['id'], tr['args'])
    for ac in data['actions']:
        mod.addAction(ac['id'], ac['args'], bot)
    return mod


class Module:
    globalVars = {}
    lockdown = False
    msg = 0
    join = 1
    sch = 2

    def __init__(self, name, modType, activated, variables):
        self.name = name
        self.modType = modType
        self.activated = activated
        self.vars = variables
        self.triggers = []
        self.actions = []

    def check(self, data):
        for trigger in self.triggers:
            if not trigger.check(data, self.vars):
                return False
        return True

    async def execute(self, data):
        for action in self.actions:
            varData = await action.execute(data)
            if varData:
                for key, elem in varData.items():
                    self.vars[key] = elem

    def addTrigger(self, trType, args):
        tr = TriggerManager.genTrigger(trType, args)
        if not tr:
            print("error de formato en el trigger de tipo", trType)
        else:
            self.triggers.append(tr)

    def addAction(self, acType, args, bot):
        ac = ActionManager.genAction(acType, args, bot)
        if not ac:
            print("error de formato en el action de tipo", acType)
        else:
            self.actions.append(ac)

    def serialize(self):
        dmod = {"type": self.modType, "activated": self.activated, "triggers": [], "actions": []}
        for trigger in self.triggers:
            dtrig = trigger.serialize
            dmod['triggers'].append(dtrig)
        for action in self.actions:
            dact = action.serialize
            dmod['actions'].append(dact)
        return dmod
