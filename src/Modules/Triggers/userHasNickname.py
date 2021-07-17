from src.Modules.trigger import TriggerManager


@TriggerManager.triggerClass
class UserHasNickname:
    def __init__(self, args):
        self.nick = args['nick']

    def check(self, data, variables):
        if data.get('member'):
            return data['member'].nick == self.nick
        return False

    def serialize(self):
        return {
            'id': UserHasNickname.__name__,
            'args': {
                'nick': self.nick
            }
        }
