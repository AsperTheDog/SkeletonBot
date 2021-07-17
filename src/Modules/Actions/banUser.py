from src.Modules.action import ActionManager


@ActionManager.actionClass
class BanUser:
    def __init__(self, args, bot):
        self.user = args['userId']

    async def execute(self, data):
        if self.user == 0:
            await data['member'].ban()
        else:
            await self.client.get_member(self.user).ban()

    def serialize(self):
        return {
            'id': BanUser.__name__,
            'args': {
                'userId': self.user
            }
        }