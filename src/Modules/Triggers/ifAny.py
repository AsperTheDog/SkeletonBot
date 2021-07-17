from src.Modules.trigger import TriggerManager


@TriggerManager.triggerClass
class IfAny:
    def __init__(self, args):
        self.triggers = []
        for arg in args:
            self.triggers.append(TriggerManager.genTrigger(arg['id'], arg['args']))

    def check(self, data, variables):
        for trigger in self.triggers:
            if trigger.check(data, variables):
                return True
        return False

    def serialize(self):
        return {
            'id': IfAny.__name__,
            'args': [tr.serialize() for tr in self.triggers]
        }
