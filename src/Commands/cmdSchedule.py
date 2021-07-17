from discord.ext import tasks
from discord.ext.commands import Cog

from src.Modules.module import Module


class schedules(Cog):
    def __init__(self, bot):
        self.client = bot
        self.scheduler.start()

    @Cog.listener()
    async def on_message(self, message):
        if message.author.bot or Module.lockdown:
            return
        data = {'message': message, 'member': message.author}
        for module in self.client.modules:
            if module.modType == Module.msg:
                if module.check(data) and module.activated:
                    data['vars'] = module.vars
                    await module.execute(data)

    @Cog.listener()
    async def on_member_join(self, member):
        if Module.lockdown:
            return
        data = {'member': member}
        for module in self.client.modules:
            if module.modType == Module.join:
                if module.check(data) and module.activated:
                    data['vars'] = module.vars
                    await module.execute(data)

    @tasks.loop(minutes=1)
    async def scheduler(self):
        if Module.lockdown:
            return
        for module in self.client.modules:
            if module.modType == Module.sch:
                if module.check({'vars': module.vars}) and module.activated:
                    await module.execute({'vars': module.vars})
