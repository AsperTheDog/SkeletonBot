import config
import os
from os import listdir
import utility
import discord
import Trigger

def checkArgs(mode, args):
    if config.openModule[-1].mode == utility.getModType("message"):
        if checkMode(mode) == 0:
            if len(args) != 2:
                return False
        elif checkMode(mode) == 1:
            if len(args) != 1:
                return False
        elif checkMode(mode) == 2:
            if len(args) != 2:
                return False
        elif checkMode(mode) == 3:
            if len(args) < 1:
                return False
    return True

def checkMode(mode):
    if config.openModule[-1].mode == utility.getModType("message"):
        if mode == "message" or mode == "m" or mode == "0":
            return 0
        elif mode == "username" or mode == "u" or mode == "1":
            return 1
        elif mode == "variable" or mode == "v" or mode == "2":
            return 2
        elif mode == "command" or mode == "c" or mode == "3":
            return 3

@config.client.command()
async def crTrigger(ctx, *args):
    if len(config.openModule) == 0:
        await ctx.channel.send(embed=utility.getEmbed("Error: No module is open, please open a module first with .OpenModule [.om]"))
        return
    argl = list(args)
    if len(argl) < 2:
        await ctx.channel.send(embed=utility.getEmbed("Error: Invalid arguments"))
        return
    name = argl.pop(0)
    mode = argl.pop(0)
    if not checkArgs(mode, argl):
        await ctx.channel.send(embed=utility.getEmbed("Error: Invalid arguments"))
        return
    n = Trigger.Trigger(name, checkMode(mode), config.openModule[-1], argl)
    config.openModule[-1].addTrigger(n)
    await ctx.channel.send(embed=utility.getEmbed("Created Trigger"))
