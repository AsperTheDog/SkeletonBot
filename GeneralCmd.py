import config
import utility

@config.client.command()
async def debug(ctx):
    await ctx.channel.send("Debug works")

@config.client.command()
async def die(ctx):
    f = open("DeathCounter.txt", "r")
    num = f.read()
    num = int(num) + 1
    f.close()
    f = open("DeathCounter.txt", "w")
    f.write(str(num))
    await ctx.channel.send(embed=utility.getEmbed("I have died " + str(num) + " times"))
    await config.client.logout()

