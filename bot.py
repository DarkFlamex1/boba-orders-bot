import discord
import time
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands

Client = discord.Client()
client = commands.Bot(command_prefix = "!")


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('token')


#import json
#oba_list = json.loads(open('boba_list.json').read())