# Begin Imports

import discord
from discord.ext import commands

# End Imports

# Begin Definitions

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
TOKEN = open("token.txt","r").read()

# End Definitions

#Main Code Begin

# Events Begin

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_member_join(member):
    channel = client.get_channel(1169097169970671737)
    await channel.send(f'Welcome {member} , hope you enjoy the server')

@client.event
async def on_member_remove(member):
    channel = client.get_channel(1169097169970671737)
    await channel.send(f'{member} Just left the server, Press F')

# Events End

#Commands begin

@client.command()
async def hello(ctx):
    await ctx.send(f'Hello, {ctx.author} I\'m Marceline Bot')

@client.command(pass_context = True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await channel.send(f'{ctx.author} I can\'t Join in to that Channel')

@client.command(pass_context = True)
async def left(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send(f'{ctx.author} I had left the channel')
    else:
        await ctx.send(f'{ctx.author} I can\'t leave a channel where i\'m not in')

#commands End


client.run(TOKEN)