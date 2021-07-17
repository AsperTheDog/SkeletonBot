from src.Modules.action import ActionManager
from src.Modules.trigger import TriggerManager
import time

@ActionManager.actionClass
class While:
    def __init__(self, args, bot):
        self.sleep = max(1, args['sleep'])
        self.client = bot
        self.actions = []
        for action in args['actions']:
            self.actions.append(ActionManager.genAction(action['id'], action['args'], self.client))
        self.conds = []
        for trigger in args['conds']:
            self.actions.append(TriggerManager.genTrigger(trigger['id'], trigger['args']))

    async def execute(self, data):
        for i in range(self.times):
            for action in self.actions:
                data['loopCount'] = i
                await action.execute(data)
                time.sleep(self.sleep)

    def serialize(self):
        return {
            'id': While.__name__,
            'args': {
                'times': self.times,
                'sleep': self.sleep,
                'actions': [ac.serialize() for ac in self.actions]
            }
        }