import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я эко  бот {bot.user}!')

@bot.command()
async def Save(ctx):
    await ctx.send("https://standfortrees.org help your tree friend")

@bot.command()
async def Greenbuy(ctx):
    await ctx.send("https://www.onyalife.com/eco-friendly-products/ no plastic only organic product")

@bot.command()
async def Glass(ctx):
    await ctx.send("Glass is not a resikling product, it is only if it made of mixt glas with calcium")

@bot.command()
async def ruber(ctx):
    await ctx.send("Ruber can be resicled")

@bot.command()
async def dev(ctx):
    await ctx.send("these bot has been developet by VladBOBO, code made by VladBOBO")

bot.run("ТУТ СЕКРЕТНЫЙ ТОКЕН")