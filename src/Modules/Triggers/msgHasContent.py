from src.Modules.trigger import TriggerManager


@TriggerManager.triggerClass
class MsgHasContent:
    def __init__(self, args):
        self.content = args['content']

    def check(self, data, variables):
        if data.get('message'):
            return self.content in data['message'].content or self.content == data['message'].content
        return False

    def serialize(self):
        return {
            'id': MsgHasContent.__name__,
            'args': {
                'content': self.content
            }
        }
