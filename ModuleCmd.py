import config
import os
from os import listdir
import utility
import Module
import discord

def ActivateModule(moduleName):
    if(moduleName in config.activeModules):
        return utility.getEmbed("Already activated")
    for x in config.modules:
        if moduleName == x.getName():
            config.activeModules.append(moduleName)
            RefreshModules(config.activeModules)
            return utility.getEmbed("Activated Module")

    return utility.getEmbed("Error, that module doesn't exist")

def DeactivateModule(moduleName):
    if(moduleName not in config.activeModules):
        return utility.getEmbed("Not activated")
    for x in config.modules:
        if moduleName == x.getName():
            config.activeModules.remove(moduleName)
            RefreshModules(config.activeModules)
            return utility.getEmbed("Dectivated Module")

    return utility.getEmbed("Error, that module doesn't exist")
    RefreshModules(config.activeModules)


def PrintModules(list):
    embed = discord.Embed(title="Modules", color=0x00ff00)
    i = 1
    string = ""
    for x in list:
        string +="**" + str(i) + ":** " + x.getName() + " - (" + utility.GetModType(x.getMode()) + ")\n"
        i += 1
    if (len(list) == 0):
        string = "There are no defined modules"
    embed.add_field(name="-------------------", value=string, inline = True)
    return embed

def PrintActiveModules():
    embed = discord.Embed(title="Active Modules", color=0x00ff00)
    i = 1
    string = ""
    for x in config.activeModules:
        string +="**" + str(i) + ":** " + x + "\n"
        i += 1
    embed.add_field(name="-------------------", value=string, inline = True)
    return embed

def LoadActiveModules():
    AM = []
    f = open("ModList.txt","r")
    lines = f.readlines()
    for x in lines:
        s = utility.SplitCommand(x)
        AM.append(s[0])
    f.close()
    return AM

def LoadModules():
    i = 0
    Modules = []    
    for x in listdir("Modules"):
        f = open("Modules\\" + x, "r")
        lines = f.readlines()
        for x in lines:
            if(x == ""): i+=1
            if(i==0):
                c = utility.SplitCommand(x)
                Modules.append(Module.Module(c[0],c[1]))
            #if(i==1):
                #check type
                #append triggers to module.
        f.close()
    return Modules

def RefreshModules(list):
    f = open("ModList.txt","w")
    for x in list:
        f.write(x + '"\n')
    f.close()

#-------------------#
#  Module Commands  #
#-------------------#

@config.client.command()
async def ModuleActivate(ctx, name):
    await ctx.channel.send(embed=ActivateModule(name))

@config.client.command()
async def ModuleDeactivate(ctx, name):
    await ctx.channel.send(embed=DeactivateModule(name))

@config.client.command()
async def crMod(ctx, name, type):
    dirs = os.listdir("Modules")
    if utility.GetModType(type) == "noType":
        response = utility.getEmbed("**Error creating the module:** Invalid type")
        await ctx.send(embed=response)
        return
    if name in dirs:
        response = utility.getEmbed("**Error creating the module:** There is already a module with that name")
        await ctx.send(embed=response)
        return
    f = open("Modules\\" + name, "w")    
    f.write(name + '"' + utility.GetModType(type) + '"\n')
    f.close()
    config.modules.append(Module.Module(name, utility.GetModType(type)))
    response = utility.getEmbed("Created module **' " + name + "'** with type **" + utility.GetModType(type) + "**")
    await ctx.send(embed=response)

@config.client.command()
async def ListModules(ctx):
    await ctx.channel.send(embed=PrintModules(config.modules))

@config.client.command()
async def ListActiveModules(ctx):
    await ctx.channel.send(embed=PrintActiveModules())

@config.client.command()
async def ModuleCheckState(ctx, name):
    if name in config.activeModules:
        await ctx.channel.send(embed=utility.getEmbed("Active"))
    else:
        await ctx.channel.send(embed=utility.getEmbed("Not Active"))

@config.client.command()
async def OpenModule(ctx, name):
    if(config.openModule != 0):
        await ctx.channel.send(embed=utility.getEmbed("**Error:** A module is already opened"))
        return
    for x in config.modules:
        if x.getName() == name:

            config.openModule = x
            await ctx.channel.send(embed=utility.getEmbed("Module **" + name + "** opened"))
            return
    await ctx.channel.send(embed=utility.getEmbed("**Error:** That module doesn't exist"))
    
@config.client.command()
async def CloseModule(ctx):
    if(config.openModule == 0):
        await ctx.channel.send(embed=utility.getEmbed("**Error:** No module opened"))
        return
    for x in config.modules:
        if config.openModule.getName() == x.getName():
            config.modules.remove(x)
    config.modules.append(config.openModule)
    config.openModule = 0
    await ctx.channel.send(embed=utility.getEmbed("Module Closed"))
    return

@config.client.command()
async def ShowOpenModule(ctx):
    if config.openModule == 0:
        string = utility.getEmbed("No module is open")
    else:
        string = utility.getEmbed("The module **" + config.openModule.getName() + "** is opened")
    await ctx.channel.send(embed=string)

#--------------------#
#   Alias Commands   #
#--------------------#

@config.client.command()
async def ma(ctx, name):
    await ModuleActivate(ctx, name)

@config.client.command()
async def md(ctx, name):
    await ModuleDeactivate(ctx, name)

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