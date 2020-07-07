import config
import os
from os import listdir
import utility
import Module
import discord
import pickle

def getModules(type):
    if type == utility.getModType("0"):
        return config.messageMod.actions
    elif type == utility.getModType("1"):
        return config.scheduleMod.actions
    elif type == utility.getModType("2"):
        return config.joinMod.actions
    else:
        return config.joinMod.actions + config.scheduleMod.actions + config.messageMod.actions

def PrintModules(list):
    embed = discord.Embed(title="Modules", color=0x00ff00)
    i = 1
    string = ""
    for x in list:
        string +="**" + str(i) + ":** " + x.getName() + " - (" + utility.getModType(x.getMode()) + ")\n"
        i += 1
    if (len(list) == 0):
        string = "There are no defined modules"
    embed.add_field(name="-------------------", value=string, inline = True)
    return embed

def PrintActiveModules():
    embed = discord.Embed(title="Active Modules", color=0x00ff00)
    i = 1
    string = ""
    for x in getModules(-1):
        if x.active == 1:
            string += "**" + str(i) + ":** " + x.getName() + " - (" + utility.getModType(x.getMode()) + ")\n"
            i += 1
    if (string == ""):
        string = "There are no active modules"
    embed.add_field(name="-------------------", value=string, inline = True)
    return embed

def createMod(name, mode):
    return Module.Module(name, mode)

def updateData(mode):
    if utility.getModType(mode) == utility.getModType("0"):
        with open("msgModuleDat.p", "wb") as f:
            pickle.dump(config.messageMod, f)
    elif utility.getModType(mode) == utility.getModType("1"):
        with open("schModuleDat.p", "wb") as f:
            pickle.dump(config.scheduleMod, f)
    elif utility.getModType(mode) == utility.getModType("2"):
        with open("joinModuleDat.p", "wb") as f:
            pickle.dump(config.joinMod, f)

def filterActions(list):
    aux = []
    for x in list:
        if isinstance(x, Module.Module):
            aux.append(x)
    return aux

#-------------------#
#  Module Commands  #
#-------------------#

@config.client.command()
async def setActiveModule(ctx, set):
    if len(config.openModule) == 0:
        await ctx.channel.send(embed=utility.getEmbed("There is no open module"))
        return
    if set == "enable":
        activity = 1
    elif set == "disable":
        activity = 0
    else:
        set == abs(config.openModule[-1].active - 1)
    config.openModule[-1].active = activity
    response = utility.getEmbed("The module **" + config.openModule[-1].name + "** is now " + set + "d")
    await ctx.send(embed=response)
    
@config.client.command()
async def crMod(ctx, name, type):
    if len(config.openModule) != 0:
        type = config.openModule[-1].mode
    else:
        father = 0
    if utility.getModType(type) == "noType":
        response = utility.getEmbed("**Error creating the module:** Invalid type")
        await ctx.send(embed=response)
        return
    for x in getModules(-1):
        if x.name == name:
            response = utility.getEmbed("**Error creating the module:** There is already a module with that name")
            await ctx.send(embed=response)
            return
    config.openModule.append(Module.Module(name, utility.getModType(type)))
    response = utility.getEmbed("Created module **' " + name + "'** with type **" + utility.getModType(type) + "**")
    await ctx.send(embed=response)

@config.client.command()
async def ListModules(ctx):
    await ctx.channel.send(embed=PrintModules(getModules(-1)))

@config.client.command()
async def ListActiveModules(ctx):
    await ctx.channel.send(embed=PrintActiveModules())

@config.client.command()
async def ModuleCheckState(ctx):
    if len(config.openModule) == 0:
        await ctx.channel.send(embed=utility.getEmbed("There is no open module"))
        return
    if config.openModule[-1].active == 1:
        await ctx.channel.send(embed=utility.getEmbed("Active"))
    else:
        await ctx.channel.send(embed=utility.getEmbed("Not Active"))

@config.client.command()
async def OpenModule(ctx, name):
    if len(config.openModule) != 0:
        list = filterActions(config.openModule[-1].actions)
    else:
        list = getModules(3)
    for x in list:
        if not isinstance(x, Module.Module):
            continue
        if x.name == name:
            config.openModule.append(x)
            await ctx.channel.send(embed=utility.getEmbed("Module **" + name + "** opened"))
            return
    if len(config.openModule) != 0:
        await ctx.channel.send(embed=utility.getEmbed("**Error:** That module doesn't exist in module **" + config.openModule[-1].name + "**"))
    else:
        await ctx.channel.send(embed=utility.getEmbed("**Error:** That module doesn't exist"))
    
@config.client.command()
async def CloseModule(ctx):
    if len(config.openModule) == 0:
        await ctx.channel.send(embed=utility.getEmbed("**Error:** No module opened"))
        return
    aux = config.openModule.pop()
    if len(config.openModule) == 0:
        if utility.getModType(aux.mode) == utility.getModType("0"):
            for x in config.messageMod.actions:
                if aux.getName() == x.getName():
                    config.messageMod.actions.remove(x)
                    break
            config.messageMod.actions.append(aux)
        elif utility.getModType(aux.mode) == utility.getModType("1"):
            for x in config.scheduleMod.actions:
                if aux.getName() == x.getName():
                    config.scheduleMod.actions.remove(x)
                    break
            config.scheduleMod.actions.append(aux)
        elif utility.getModType(aux.mode) == utility.getModType("2"):
            for x in config.joinMod.actions:
                if aux.getName() == x.getName():
                    config.joinMod.actions.remove(x)
                    break
            config.joinMod.actions.append(aux)
        else:
            print("Invalid type wtf this should not happen O.o\n")
            return
        updateData(aux.mode)
    else:
        for x in filterActions(config.openModule[-1].actions):
            if aux.getName() == x.getName():
                config.openModule[-1].actions.remove(x)
                break
        config.openModule[-1].actions.append(aux)
    await ctx.channel.send(embed=utility.getEmbed("Module Closed"))
    return

@config.client.command()
async def ShowOpenModule(ctx):
    if len(config.openModule) == 0:
        string = utility.getEmbed("No module is open")
    else:
        string = utility.getEmbed("The module **" + config.openModule[-1].getName() + "** is opened")
    await ctx.channel.send(embed=string)

@config.client.command()
async def DeleteModule(ctx):
    if len(config.openModule) == 0:
        await ctx.channel.send(embed=utility.getEmbed("No module is open"))
        return
    aux = config.openModule.pop()
    if len(config.openModule) == 0:
        for x in getModules(aux.mode):
            if x.name == aux.name:
                getModules(aux.mode).remove(x)
                await ctx.channel.send(embed=utility.getEmbed("Deleted the module **" + aux.name + "**"))
                updateData(aux.mode)
                return
    for x in config.openModule[-1].actions:
        if x.name == aux.name:
            config.openModule[-1].actions.remove(x)
    await ctx.channel.send(embed=utility.getEmbed("Deleted the module **"+ aux.name + "**"))
    
    
@config.client.command()
async def DisplayModule(ctx):
    if len(config.openModule) == 0:
        await ctx.channel.send(embed=utility.getEmbed("There is no open module, use .OpenModule [.om] to open a module"))
        return
    await ctx.channel.send(config.openModule[-1].print(0))

@config.client.command()
async def SaveBackup(ctx):
    config.backup = config.openModule.copy()
    await ctx.channel.send(embed=utility.getEmbed("Backup saved, use .LoadBackup [.lb] to load it"))

@config.client.command()
async def LoadBackup(ctx):
    if config.backup == 0:
        await ctx.channel.send(embed=utility.getEmbed("There is no backup saved, use .SaveBackup [.sb] to save the current open Modules"))
        return
    config.openModule = config.backup.copy()
    await ctx.channel.send(embed=utility.getEmbed("Backup loaded"))

@config.client.command()
async def DisplayBackup(ctx):
    string = ""
    for x in config.backup:
        string += x.print(0) + "\n---------------------------\n"
    await ctx.channel.send(string)

@config.client.command()
async def CancelEdit(ctx):
    config.openModule.clear()
    await ctx.channel.send(embed=utility.getEmbed("Closed modules without saving"))

#--------------------#
#   Alias Commands   #
#--------------------#

@config.client.command()
async def am(ctx, name):
    await setActiveModule(ctx, name)

@config.client.command()
async def lm(ctx):
    await ListModules(ctx)

@config.client.command()
async def lam(ctx):
    await ListActiveModules(ctx)

@config.client.command()
async def om(ctx, name):
    await OpenModule(ctx, name)

@config.client.command()
async def cm(ctx):
    await CloseModule(ctx)

@config.client.command()
async def som(ctx):
    await ShowOpenModule(ctx)

@config.client.command()
async def delm(ctx):
    await DeleteModule(ctx)

@config.client.command()
async def dpm(ctx):
    await DisplayModule(ctx)

@config.client.command()
async def sb(ctx):
    await SaveBackup(ctx)

@config.client.command()
async def lb(ctx):
    await LoadBackup(ctx)

@config.client.command()
async def dpb(ctx):
    await DisplayBackup(ctx)

@config.client.command()
async def ce(ctx):
    await CancelEdit(ctx)
