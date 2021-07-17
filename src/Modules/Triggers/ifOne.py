from src.Modules.trigger import TriggerManager


@TriggerManager.triggerClass
class IfOne:
    def __init__(self, args):
        self.triggers = []
        for arg in args:
            self.triggers.append(TriggerManager.genTrigger(arg['id'], arg['args']))

    def check(self, data, variables):
        occ = 0
        for trigger in self.triggers:
            if trigger.check(data, variables):
                occ += 1
        return occ == 1

    def serialize(self):
        return {
            'id': IfOne.__name__,
            'args': [tr.serialize() for tr in self.triggers]
        }
