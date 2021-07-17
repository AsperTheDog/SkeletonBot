from discord import Embed, Colour
from discord.ext.commands import has_permissions, Cog, command

from src.Modules.module import Module

pingHelpLong = "Command to get the latency of the bot, use this to see if SkeletonBot is alive"
killHelpLong = "Command to shut down SkeletonBot. If configured to do so, the bot will restart inmediately after"
lockdownHelpLong = "Command to inmediately deactivate all modules and stop them from working. Use this if you fucked up with a module and SkeletonBot is going rampage"
unlockdownHelpLong = "Command to disable the lockdown when activated by the command .quarantine"
setGlobalHelpLong = "Command to set the value of an existing value or create a new one if it doesn't exist"


class stdCommands(Cog, name="General"):
    def __init__(self, bot):
        self.bot = bot

    @command(brief="Ping", description="Everyone", help=pingHelpLong)
    async def ping(self, ctx):
        print(self.ping.signature)
        await ctx.channel.send(embed=Embed(description=":ping_pong:   **{0}**".format(int(self.bot.latency * 1000)), color=Colour.blue()))

    @command(aliases=['shutdown', 'kill'], brief="Shut down Bot", description="Admin only", help=killHelpLong)
    @has_permissions(administrator=True)
    async def die(self, ctx):
        await ctx.channel.send(embed=Embed(description="Shuting down...", color=Colour.blue()))
        await self.bot.logout()

    @command(aliases=['lock', 'lk', 'lockdown'], brief="Emergency bot lockdown", description="Admin only", help=lockdownHelpLong)
    @has_permissions(administrator=True)
    async def quarantine(self, ctx):
        await ctx.channel.send(embed=Embed(description="Lockdown activated, no module will execute", color=Colour.red()))
        Module.lockdown = True

    @command(aliases=['unlock', 'ulk'], brief="Disable Emergency bot lockdown", description="Admin only", help=lockdownHelpLong)
    @has_permissions(administrator=True)
    async def unquarantine(self, ctx):
        await ctx.channel.send(embed=Embed(description="Lockdown deactivated, modules will execute again", color=Colour.blue()))
        Module.lockdown = False

    @command(aliases=['sgv'], brief="Set the value of a global variable", description="Everyone", help=setGlobalHelpLong)
    async def setGlobalVar(self, name, value, varType):
        if varType != 'str':
            exec("value = %s(value)" % varType)
        Module.globalVars[name] = value
