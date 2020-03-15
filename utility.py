import Module
import discord

def SplitCommand(command):
    aux = command
    sp = aux.split('"')
    i = 0
    while ' ' in sp:
        sp.remove(' ')
    return sp

def GetModType(str):
    if str == "m" or str == "message" or str == "0":
        return "message"
    if str == "s" or str == "schedule" or str == "1":
        return "schedule"
    if str == "j" or str == "join" or str == "2":
        return "join"
    return "noType"

def getEmbed(str):
    embed = discord.Embed(title=str, color=0x00ff00)
    return embed