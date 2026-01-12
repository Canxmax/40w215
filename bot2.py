import discord
from discord.ext import commands
import os, random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def As(ctx):
    b = 0
    while True:
        await ctx.send("çöpünüz:")
        await ctx.send(b)
        b += 1
        if b == 10:
            await ctx.send("çöp doldu")
            break
    




bot.run('RaHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH')
