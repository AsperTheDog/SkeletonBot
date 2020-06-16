import config
import os
from os import listdir
import utility
import discord
import Trigger


@config.client.command()
async def crTrigger(ctx, *args):
    if config.openModule == 0:
        await ctx.channel.send(embed=utility.getEmbed("Error: No module is open, please open a module first with\n*.om <Module name>*"))
    argl = list(args)
    name = argl.pop(0)
    mode = argl.pop(0)
    n = Trigger.Trigger(name, mode, argl)
    config.openModule[-1].addTrigger(n)
    await ctx.channel.send(embed=utility.getEmbed("Created Trigger"))
