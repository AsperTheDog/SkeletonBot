import config
import utility
import pickle

@config.client.command()
async def debug(ctx):
    await ctx.channel.send(config.messageMod.print(0))
    await ctx.channel.send("------------------------------------------")
    await ctx.channel.send(config.scheduleMod.print(0))
    await ctx.channel.send("------------------------------------------")
    await ctx.channel.send(config.joinMod.print(0))

@config.client.command()
async def die(ctx):
    with open("deathcounter.p", "rb") as f:
        num = pickle.load(f)
    num = int(num) + 1
    with open("deathcounter.p", "wb") as f:
        pickle.dump(num, f)
    await ctx.channel.send(embed=utility.getEmbed("I have died " + str(num) + " times"))
    await config.client.logout()

@config.client.command()
async def toggleMainteinance(ctx):
    if config.mainteinance == 0:
        config.mainteinance = 1
        response = utility.getEmbed("Mainteinance mode is now on, all modules disabled")
        await ctx.send(embed=response)
    else:
        config.mainteinance = 0
        response = utility.getEmbed("Mainteinance mode is now of, normal configurations restored")
        await ctx.send(embed=response)
