from src.Modules.action import ActionManager
import time

@ActionManager.actionClass
class Loop:
    def __init__(self, args, bot):
        self.times = max(1, args['times'])
        self.sleep = max(1, args['sleep'])
        self.client = bot
        self.actions = []
        for action in args['actions']:
            self.actions.append(ActionManager.genAction(action['id'], action['args'], self.client))

    async def execute(self, data):
        for i in range(self.times):
            for action in self.actions:
                data['loopCount'] = i
                await action.execute(data)
                time.sleep(self.sleep)

    def serialize(self):
        return {
            'id': Loop.__name__,
            'args': {
                'times': self.times,
                'sleep': self.sleep,
                'actions': [ac.serialize() for ac in self.actions]
            }
        }