# bot.py
import os
import discord
from discord.ext import commands

import config
import utility
import TriggerCmd
import ModuleCmd
import GeneralCmd

@config.client.event
async def on_ready():
    if not os.path.exists('Modules'):
        os.mkdir('Modules')
    if not os.path.exists('ModList.txt'):
        f = open("ModList.txt", "w")
        f.close()
    print(f'{config.client.user.name} has connected to Discord!')
    config.modules = ModuleCmd.LoadModules()
    config.activeModules = ModuleCmd.LoadActiveModules()

@config.client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@config.client.event
async def on_message(message):
    if message.author == config.client.user:
        return
    await config.client.process_commands(message)
    
    for x in config.modules:
        if config.openModule != 0:
            if x.getName() == config.openModule.getName():
                continue
        if x.getName() in config.activeModules:
            if x.CheckTriggers(message) == True:
                # Ejecutar acciones

config.client.run(config.token)
