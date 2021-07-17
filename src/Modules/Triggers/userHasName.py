from src.Modules.trigger import TriggerManager


@TriggerManager.triggerClass
class UserHasName:
    def __init__(self, args):
        self.username = args['username']

    def check(self, data, variables):
        return data['user'].name == self.username

    def serialize(self):
        return {
            'id': UserHasName.__name__,
            'args': {
                'username': self.username
            }
        }
