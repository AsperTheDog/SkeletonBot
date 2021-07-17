from src.Modules.trigger import TriggerManager


@TriggerManager.triggerClass
class UserHasDiscriminator:
    def __init__(self, args):
        self.disc = args['disc']

    def check(self, data, variables):
        if data.get('user'):
            return data['user'].discriminator == self.disc
        return False

    def serialize(self):
        return {
            'id': UserHasDiscriminator.__name__,
            'args': {
                'disc': self.disc
            }
        }
