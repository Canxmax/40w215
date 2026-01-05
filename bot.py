import discord
from discord.ext import commands
import os, random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

b = 0
a = True
@bot.command()
async def As(ctx):
    b = 0
    a = True
    while a:
        await ctx.send(b)
        b += 1
        if b == 10:
            a = False




bot.run('NO TOKEN FOR U!!!!!!!!!')
