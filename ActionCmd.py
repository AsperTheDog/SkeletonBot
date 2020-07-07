import config
import os
from os import listdir
import utility
import discord
import Action

def checkArgs(mode, args):
    if checkMode(mode) == 0:
        if len(args) != 1:
            return False
    if checkMode(mode) == 1:
        if len(args) != 2:
            return False
    if checkMode(mode) == 2:
        if len(args) != 2:
            return False
    if checkMode(mode) == 3:
        if len(args) != 3:
            return False
    return True

def checkMode(mode):
    if config.openModule[-1].mode == utility.getModType("message"):
        if mode == "message" or mode == "0" or mode == "m":
            return 0
        elif mode == "giverole" or mode == "1" or mode == "gr":
            return 1
        elif mode == "removerole" or mode == "2" or mode == "rr":
            return 2
        elif mode == "variable" or mode == "3" or mode == "v":
            return 3

@config.client.command()
async def crAction(ctx, *args):
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
    n = Action.Action(name, config.openModule[-1], checkMode(mode), argl)
    config.openModule[-1].addAction(n)
    await ctx.channel.send(embed=utility.getEmbed("Created Action"))