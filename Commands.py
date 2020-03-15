from discord.ext import commands
import bot

bot = commands.Bot(command_prefix='1')

@bot.command()
async def debug(ctx):
    response = ""
    for x in ctx.author.guild_permissions:
        response = x
        await ctx.send(response)

@bot.command()
async def crMod(ctx, arg1, arg2):
    dirs = os.listdir("Modules")
    if arg1 in dirs:
        response = "**Error creating the module:** There is already a module with that name"
        await ctx.send(response)
        return
    f = open("Modules\\" + arg1, "w")    
    f.write(arg1 + '"')
    f.write(arg2 + '"')
    f.write("\n")
    f.close()
    bot.modules.append(Module.Module(arg1, arg2))
    bot.activeModules.append(arg1)
    utility.RefreshModules(bot.activeModules)        
    response = "Created module **' " + arg1 + "'** with type **" + utility.GetModType(arg2) + "**"
    await ctx.send(response)

def setup(bot):
    bot.add_command(debug)
    bot.add_command(crMod)