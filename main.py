""""
In order to run this proyect, you'll need your ChatGPT API Key, ProjectID, OrganizationID, and Discord Bot token
"""

import discord
from discord.ext import commands
import os, asyncio

#import all the cogs
from help_cog import help_cog
from music_cog import music_cog
from gpt_cog import gpt_cog

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='+', intents=intents)

#remove the default help command so that we can write out own
bot.remove_command('help')

async def main():
    async with bot:
        await bot.add_cog(help_cog(bot))
        await bot.add_cog(music_cog(bot))
        await bot.add_cog(gpt_cog(bot))
        await bot.start("")

asyncio.run(main())
