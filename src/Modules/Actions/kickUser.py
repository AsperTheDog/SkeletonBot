from src.Modules.action import ActionManager


@ActionManager.actionClass
class KickUser:
    def __init__(self, args, bot):
        self.user = args['userId']

    async def execute(self, data):
        if self.user == 0:
            await data['member'].kick()
        else:
            await self.client.get_member(self.user).kick()

    def serialize(self):
        return {
            'id': KickUser.__name__,
            'args': {
                'userId': self.user
            }
        }