# bot.py
import os

import discord
from discord.ext import commands
import Module
from dotenv import load_dotenv
import random
import utility

# global
modules = []
activeModules = []

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = discord.Client()

bot = commands.Bot(command_prefix='1')
bot.load_extension('Commands')

def ActivateModule(moduleName):
    activeModules.append(moduleName)
    utility.RefreshModules(activeModules)        

def DeactivateModule(moduleName):
    activeModules.remove(moduleName)
    utility.RefreshModules(activeModules)        

@client.event
async def on_ready():
    global modules, activeModules
    if not os.path.exists('Modules'):
        os.mkdir('Modules')
    print(f'{client.user.name} has connected to Discord!')
    modules = utility.LoadModules()
    activeModules = utility.LoadActiveModules()


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )


@client.event
async def on_message(message):
    if message.author == client.user:
        return



client.run(token)
