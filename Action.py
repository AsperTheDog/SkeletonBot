import discord
import utility

class Action:
    

    def __init__(self, name, module, mode, args):
        self.name = name
        self.module = module
        self.args = args
        self.mode = mode

    async def execute(self, arg):
        if self.module.mode == utility.getModType("message"):
            await self.executeMessage(arg)
        elif self.module.mode == utility.getModType("schedule"):
            await self.executeSchedule(arg)
        elif self.module.mode == utility.getModType("join"):
            await self.executeJoin(arg)

    async def executeMessage(self, message):
        text = self.processMessage(message)
        if text != "":
            await message.channel.send(text)

    def executeSchedule(self, arg):
        pass

    def executeJoin(self, arg):
        pass

    def print(self):
        print(self.mode)
        if self.mode == 0:
            return "**" + self.name + "**: Sends the message '" + self.args[0] + "'"
        elif self.mode == 1:
            return "**" + self.name + "**: Gives the role '" + self.args[0] + "' to the user '" + self.args[1] + "'"

    def processMessage(self, message):
        text = self.args[0]
        if "%author%" in self.args[0]:
            text = text.replace("%author%", message.author.name)
        if "%variable%" in self.args[0]:
            for x in self.module.variables:
                text = text.replace("%variable%" + x + "%", self.module.variables.get(x))
        return text
