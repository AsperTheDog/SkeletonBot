from datetime import datetime, timedelta
from src.Modules.trigger import TriggerManager


@TriggerManager.triggerClass
class AfterCooldown:
    def __init__(self, args):
        self.time = args['interval']
        self.last = args['last']

    def check(self, data, variables):
        if (datetime.fromtimestamp(self.last) + timedelta(seconds=self.time)) < datetime.utcnow():
            self.last = datetime.utcnow().timestamp()
            return True

    def serialize(self):
        return {
            'id': AfterCooldown.__name__,
            'args': {
                'interval': self.time,
                'last': self.last
            }
        }
