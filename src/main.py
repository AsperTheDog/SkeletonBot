import json
import os

import dotenv
from discord.ext.commands import Bot

from Commands.cmdGeneral import stdCommands
from Commands.cmdHelp import HelpCmd
from Commands.cmdSchedule import schedules
from Modules import module

dbName = 'SkeletonBot'
colName = 'Modules'

dotenv.load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = Bot(
    command_prefix='.',
    case_insensitive=True,
    description="SkeletonBot is a customizable bot that will allow you to make your own",
    help_command=HelpCmd()
)
client.modules = []

dataPath = os.path.join(os.path.dirname(__file__), "DataFiles")

with open(os.path.join(dataPath, 'module1.json')) as file:
    data = json.load(file)
client.modules.append(module.deserialize(data, client))

with open(os.path.join(dataPath, 'module2.json')) as file:
    data = json.load(file)
client.modules.append(module.deserialize(data, client))

with open(os.path.join(dataPath, 'module3.json')) as file:
    data = json.load(file)
client.modules.append(module.deserialize(data, client))

# mongoClient = pymongo.MongoClient("localhost", 27017)
# print("connected to mongo server")
# mdb = mongoClient[dbName]
# db = mdb[colName]

client.add_cog(stdCommands(client))
client.add_cog(schedules(client))

client.run(TOKEN)
# mongoClient.close()
