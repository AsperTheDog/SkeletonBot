from src.Modules.action import ActionManager


def getAttrFromData(attr, data):
    if attr == 'msgContent':
        return data['message'].content
    elif attr == 'userId':
        return data['member'].id
    elif attr == 'userName':
        return data['member'].name
    elif attr == 'userDisc':
        return data['member'].discriminator
    elif attr == 'userNick':
        return data['member'].nick
    elif attr == 'channelId':
        return data['message'].channel.id
    elif attr == 'channelName':
        return data['message'].channel.name
    elif 'variable' in attr:
        attr = attr.split(':')[1]
        return data['vars'][attr]


@ActionManager.actionClass
class AttrToVar:
    def __init__(self, args, bot):
        self.var = args['var']
        self.attr = args['attr']

    async def execute(self, data):
        content = getAttrFromData(self.attr, data)
        return {self.var: content}

    def serialize(self):
        return {
            'id': AttrToVar.__name__,
            'args': {
                'var': self.var,
                'attr': self.attr,
            }
        }
