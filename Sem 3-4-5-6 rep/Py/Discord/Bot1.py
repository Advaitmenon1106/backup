from discord.ext import commands
from discord import Message, Intents, Guild
import random as rand


bot = commands.Bot(command_prefix="!L ", case_insensitive=True, intents=Intents.all())
token = 'MTA2MTIzNzkyNTUzMjE0MzY0Ng.GgaxKJ.A8C7H0RdOZReDMt_Kby603tb2ckI3XWcP86-qc'

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_message(message):
	await message.reply("hello!")

bot.run(token)