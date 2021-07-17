from src.Modules.action import ActionManager
from discord import Embed, Color
import re


def parsePlaceHolders(message, variables):
    msg = message
    res = re.find(r"%var:[a-zA-z0-9]+%", message)
    for inst in res:
        msg = msg.replace(inst, str(variables.get(inst.replace('%', '').split(':')[1])))
    return msg


@ActionManager.actionClass
class SendMessage:
    def __init__(self, args, bot):
        self.bot = bot
        self.content = args['content']
        self.channel = args['channel']
        self.embed = args['embed']

    async def execute(self, data):
        chArg = None
        channel = None
        if self.channel == 0:
            if data.get('message'):
                chArg = data['message'].channel
                channel = data['message'].channel
            elif data.get('member') and data['member'].guild.system_channel:
                chArg = data['member'].guild.system_channel
                channel = data['member'].guild.system_channel
        else:
            chArg = self.bot.get_channel(self.channel)
            channel = self.bot.get_channel(self.channel)

        # if not chArg or not channel:
        #     return

        content = parsePlaceHolders(self.content, data['vars'])
        if self.embed == "False":
            await channel.send(content)
        else:
            await channel.send(embed=Embed(description=content, color=Color.blue()))

    def serialize(self):
        return {
            'id': SendMessage.__name__,
            'args': {
                'content': self.content,
                'channel': self.channel
            }
        }
