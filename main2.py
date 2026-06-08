import discord
from discord.ext import commands
from model import get_class
    
intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    for i in range(count_heh):
        await ctx.send("he" * count_heh)
    await ctx.send("ha")


async def detect(ctx):
    await ctx.send(f'Algılama başladı')
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            filename = attachment.filename
            filepath = f"images/{filename}"
            await attachment.save(filepath)
            await ctx.send("ha")
    else:
        await ctx.send("Lütüfen foto yükle pls :3")

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./images/{file_name}")
            await ctx.send(f"Saved the images to ./images/{file_name}")
            result = get_class(model_path="keras_model.h5", labels_path="labels.txt", image_path=f"./images/{file_name}")

            if result[0] == "Güvercin\n":
                await ctx.send("The image is classified as: pigeon")
            elif result[0] == "Serçe\n":
                await ctx.send("The image is classified as: sparrow")

    else:
        await ctx.send("You forgot to upload the image:(")


bot.run("NO TOKEN FOR UU!!!!!!!!!!!!!!!!!!!!!!!!!!!")
