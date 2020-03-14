# bot.py
import os

import discord
import Module
from dotenv import load_dotenv
import random
from utility import SplitCommand

# global
reactComms = []
modules = []



load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    if not os.path.exists('Modules'):
        os.mkdir('Modules')
    print(f'{client.user.name} has connected to Discord!')
    global reactComms
    f = open("customReac.txt", "r")
    line = f.readlines()
    for x in line:
        command = x.split('"')
        if len(x) != 1:
            reactComms.append([command[0], command[1], command[2]])
    f.close()


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

    global reactComms, modules

    # Debug command, change it however you want to test things
    if message.content == "debug":
        response = ""
        for x in message.author.guild_permissions:
            response = x
            await message.channel.send(response)

    # Add reaction command, this will add a reaction to the list
    if message.content.find("1addr") == 0:

        # Check the user has admin perms
        if ('administrator', True) not in message.author.guild_permissions:
            response = "This command must be done by an administrator"
            await message.channel.send(response)
            return

        aux = SplitCommand(message.content)

        # Check the command has the correct amount of parameters (Command - Reaction - Reaction message - Mode - EndSegment)
        if len(aux) != 5:
            response = "Wrong Parameters for command " + aux[0]
            await message.channel.send(response)
            return

        if aux[3] != "anywhere" and aux[3] != "beginning" and aux[3] != "command":
            response = "Error: The type of reaction can only be: Anywhere/beginning/command"
            await message.channel.send(response)
            return

        f = open("customReac.txt", "r")
        line = f.readlines()

        # Check the command is not repeated
        for x in line:
            command = x.split('"')

            if command[0] == aux[1]:
                response = "Error: The reaction '**" + \
                    aux[1] + "**' already exists"
                await message.channel.send(response)
                return

        f.close()
        f = open('customReac.txt', 'a')
        aux.pop(0)

        # Write the reaction in the file
        for x in aux:
            f.write(x + '"')
        f.write("\n")
        f.close()

        f = open("customReac.txt", "r")
        line = f.readlines()

        # Look for the command in the file
        for x in line:
            command = x.split('"')
            if command[0] == aux[0]:
                found = 1
                break

        # If we find it, print it. If we don't, print error
        if found == 1:
            response = "Succesfully created reaction **" + \
                command[0] + "** with the message **'" + \
                command[1] + "'** in mode '**" + command[2] + "**'"
            await message.channel.send(response)
            reactComms.append([command[0], command[1], command[2]])
        else:
            response: "There was an error while creating the reaction (It didn't save correctly)"
            await message.channel.send(response)
        f.close()
        return

    if message.content.find("1crMod ") == 0:
        command = SplitCommand(message.content)
        modMode = command[1]
        modName = command[2]
        dirs = os.l
        modules.append(Module(modMode, modName))
        

        # Reaction execution
    for x in reactComms:
        found = False

        if x[2] == "anywhere":
            if message.content.find(x[0] + " ") != -1:
                found = True
        elif x[2] == "beginning":
            if message.content.find(x[0] + " ") == 0:
                found = True
        elif x[2] == "command":
            if message.content == x[0]:
                found == True
        if found == True:
            response = x[1]
            await message.channel.send(response)
            return

client.run(token)
