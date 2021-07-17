from src.Modules.trigger import TriggerManager


@TriggerManager.triggerClass
class UserHasId:
    def __init__(self, args):
        self.id = args['id']

    def check(self, data, variables):
        return data['user'].id == self.id

    def serialize(self):
        return {
            'id': UserHasId.__name__,
            'args': {
                'id': self.id
            }
        }
