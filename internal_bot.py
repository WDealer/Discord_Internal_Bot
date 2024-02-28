# Begin Imports

import nextcord
from nextcord.ext import commands
from nextcord import Interaction
from secret import *
import openai

# End Imports

# Begin Definitions
intents = nextcord.Intents.all()
client = commands.Bot(command_prefix="!", intents=intents)
intents.message_content = True
intents.members = True
openai.api_key = token_chatgpt

testServerId = 1169092034934603787

# End Definitions

# Main Code Begin

# Events Begin

@client.event
async def on_ready():
    await client.change_presence(status=nextcord.Status.do_not_disturb,activity=nextcord.Streaming(name='Elden Ring',url='https://www.youtube.com/watch?v=dQw4w9WgXcQ'))
    print(f'We have logged in as {client.user}')

## Join and Remove events

@client.event
async def on_member_join(member):
    channel = client.get_channel(1169097169970671737)
    await channel.send(f'Welcome {member} , hope you enjoy the server')

@client.event
async def on_member_remove(member):
    channel = client.get_channel(1169097169970671737)
    await channel.send(f'{member} Just left the server, Press F')

## Chat Bot event using Open AI

@client.event
async def on_message(message):

    if message.author == client.user:
        return
    
    if client.user in message.mentions:

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"{message.content}",
            max_tokens=2048,
            temperature=0.5,
        )

        await message.channel.send(f'{message.author.mention},{response.choices[0].text}')

# Events End

#Commands begin

@client.slash_command(name="hello",description="Hello Command for testing the bot",guild_ids=[testServerId])
async def hello(Interaction:Interaction):
    await Interaction.response.send_message(f'Hello, {str(Interaction.user.mention)} I\'m Marceline Bot')

@client.slash_command(name="Join",description="Make the bot join the channel",guild_ids=[testServerId])
async def join(Interaction:Interaction):
    if()

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


client.run(token_nextcore)