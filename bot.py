# bot.py
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import pickle

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

import config
import utility
import TriggerCmd
import ModuleCmd
import ActionCmd
import GeneralCmd

@config.client.event
async def on_ready():
    if os.path.isfile("msgModuleDat.p"):
        with open("msgModuleDat.p", "rb") as f:
            config.messageMod = pickle.load(f)
        print("message module found, restoring...")
    else:
        config.messageMod = ModuleCmd.createMod("rootM", 0)
        config.messageMod.active = 1
    if os.path.isfile("schModuleDat.p"):
        with open("schModuleDat.p", "rb") as f:
            config.scheduleMod = pickle.load(f)
        print("schedule module found, restoring...")
    else:
        config.scheduleMod = ModuleCmd.createMod("rootS", 1)
        config.scheduleMod.active = 1
    if os.path.isfile("joinModuleDat.p"):
        with open("joinModuleDat.p", "rb") as f:
            config.joinMod = pickle.load(f)
        print("join module found, restoring...")
    else:
        config.joinMod = ModuleCmd.createMod("rootJ", 2)
        config.joinMod.active = 1
    print(f'{config.client.user.name} has connected to Discord!')


@config.client.event
async def on_member_join(member):
    config.joinMod.execute(member)


@config.client.event
async def on_message(message):
    if message.author == config.client.user:
        return
    await config.client.process_commands(message)
    if config.mainteinance == 0:
        await config.messageMod.execute(message)

config.client.run(token)
