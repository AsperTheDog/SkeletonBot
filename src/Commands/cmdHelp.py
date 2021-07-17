from discord import Embed, Colour
from discord.ext.commands import HelpCommand

foot = "For more information about a command or module, use .help followed by its name/alias"
helpHelp = "Use this command without arguments to get the list of modules. Add the name of a module as argument to get the list of commands of that module. Add the name of a command instead of a module to get info of the command (like you just did)"


class HelpCmd(HelpCommand):
    def __init__(self):
        super().__init__(command_attrs={"aliases": ['h', 'info'], "brief": "Help Command", "description": "Everyone", "help": helpHelp})

    def get_command_signature(self, command):
        return '{0.clean_prefix}{1.qualified_name} {1.signature}'.format(self, command)

    async def send_bot_help(self, mapping):
        embed = Embed(title="Modules of the bot", color=Colour.blue())
        string = ""
        for mapArg in mapping:
            if mapArg:
                string += "- " + mapArg.qualified_name + "\n"
        if string == "":
            string = "No modules made yet"
        embed.add_field(name="-----------------------", value=string, inline=False)
        embed.set_footer(text=foot)
        await self.get_destination().send(embed=embed)

    async def send_cog_help(self, cog):
        embed = Embed(title="Commands in module " + cog.qualified_name, color=Colour.blue())
        string = "```"
        for command in cog.get_commands():
            string += "- " + str(command) + " ["
            for alias in command.aliases:
                if alias == command.aliases[-1]:
                    string += alias
                else:
                    string += alias + ", "
            string += "]\n"
        string += " ```"
        if string == "``` ```":
            string = "```There are no commands in this module```"
        embed.add_field(name="Commands", value=string)
        embed.set_footer(text=foot)
        await self.get_destination().send(embed=embed)

    async def send_command_help(self, command):
        if command.cog_name:
            embed = Embed(title=command.brief, description="**From the module " + command.cog_name + "**", color=Colour.blue())
        else:
            embed = Embed(title=command.brief, color=Colour.blue())
        embed.add_field(name="1. Usage", value=command.help, inline=False)
        embed.add_field(name="2. Format", value=self.get_command_signature(command), inline=False)
        embed.add_field(name="3. Aliases", value=str(command.aliases).replace("'", ""), inline=False)
        embed.add_field(name="3. Permissions", value=command.description, inline=False)
        embed.set_footer(text=foot)
        await self.get_destination().send(embed=embed)

    async def command_not_found(self, string):
        embed = Embed(title="Command/Module not found",
                      description="The command/module **" + string + "** was not found. Use help without arguments to see the list of commands",
                      color=Colour.blue())
        return embed

    async def send_error_message(self, error):
        if isinstance(error, Embed):
            await self.get_destination().send(embed=error)
        else:
            await self.get_destination().send(error)
