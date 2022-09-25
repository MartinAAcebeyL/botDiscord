from decouple import config
from discord.ext import commands
import discord

intents = discord.Intents.all()#para habilitar o desabilitar funciones de la api
intents.message_content = True


client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We are ready !!! {client.user}, {client}')
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send(f'Hello!,{message.author}, how are you?')

    if message.content.startswith('$by'):
        await message.channel.send(f'By!,{message.author}, i hope you have a nice day?')

@client.event
async def on_message_edit(before, after):
    await before.channel.send(before.content)

@client.event
async def on_message_delete(message):
    await message.channel.send(f" {message.author} elimino: => {message.content}")

client.run(config('TOKEN_DISCORD'))