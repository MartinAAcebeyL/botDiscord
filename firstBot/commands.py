from decouple import config
from discord.ext import commands
import discord

intents = discord.Intents.all()#para habilitar o desabilitar funciones de la api
intents.message_content = True

bot = commands.Bot(command_prefix='>', intents=intents, description="desripton")

# Comandos

@bot.event
async def on_ready():
    print('comandos preparados')

@bot.command()
async def mimo(ctx, arg):
    await ctx.send(f"mimo dice: {arg}") 

@bot.command()
async def risa(ctx):
    await ctx.send("ajajjaj")

bot.run(config('TOKEN_DISCORD'))