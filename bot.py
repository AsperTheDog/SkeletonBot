# bot.py
import os
from dotenv import load_dotenv
load_dotenv()

from discord.ext import commands

import config
import Module
import utility

def ActivateModule(moduleName):
    config.activeModules.append(config.moduleName)
    utility.RefreshModules(config.activeModules)        

def DeactivateModule(moduleName):
    config.activeModules.remove(moduleName)
    utility.RefreshModules(config.activeModules)  

@config.client.event
async def on_ready():
    if not os.path.exists('Modules'):
        os.mkdir('Modules')
    print(f'{config.client.user.name} has connected to Discord!')
    modules = utility.LoadModules()
    activeModules = utility.LoadActiveModules()
    config.client.load_extension('Commands')

@config.client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@config.client.event
async def on_message(message):

    await config.client.process_commands(message)

#Commands
@config.client.command()
async def debug(ctx):
    await ctx.channel.send("Debug works")

@config.client.command()
async def die(ctx):
    await config.client.logout()

@config.client.command()
async def crMod(ctx, arg1, arg2):
    dirs = os.listdir("Modules")
    if arg1 in dirs:
        response = "**Error creating the module:** There is already a module with that name"
        await ctx.send(response)
        return
    f = open("Modules\\" + arg1, "w")    
    f.write(arg1 + '"')
    f.write(arg2 + '"')
    f.write("\n")
    f.close()
    config.modules.append(Module.Module(arg1, arg2))
    config.activeModules.append(arg1)
    utility.RefreshModules(config.activeModules)        
    response = "Created module **' " + arg1 + "'** with type **" + utility.GetModType(arg2) + "**"
    await ctx.send(response)

config.client.run(os.getenv('DISCORD_TOKEN'))
