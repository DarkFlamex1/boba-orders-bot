import discord
import time
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import json

orders = []
BOBA_LIST = json.loads(open('boba_list.json').read())
config = json.load(open("./token.json", "r"))

Client = discord.Client()
client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_member_join(self, member):
    guild = member.guild
    if guild.system_channel is not None:
        to_send = '{0.mention} has left {1.name} :cry:'.format(member, guild)
        await guild.system_channel.send(to_send)

@client.event    
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    
    cmd = message.content
    if cmd.startswith('!commands'):
        print('!hello, !cookie, !cookies, and !order')
    
    elif cmd.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(message.channel, msg)
    
    elif cmd == '!cookie':
        await message.channel.send(':cookie:')
        print("cookie called")
    elif cmd == '!cookies':
        await message.channel.send(":cookie::cookie::cookie::cookie::cookie::cookie:" +
                                    ":cookie::cookie::cookie::cookie::cookie::cookie:" +
                                    ":cookie::cookie::cookie::cookie::cookie::cookie:")
        print("cookies called")
    
    elif cmd == '!clear list':
        orders = []
    
    elif cmd == '!print list':
        await message.channel.send(orders)
    
    elif cmd[0:6] == '!order':
        print('order called')
        # get name of boba by removing '!order'
        cmd = cmd[7:]
        if cmd.lower() in BOBA_LIST:
            await message.channel.send('Your order for ' + cmd + ' has been placed')
            orders.append(cmd)
            print("boba ordered")
        else:
            await message.channel.send('Your order for ' + cmd + ' has failed to be placed')

# run the bot
try:
    client.run(config["token"])
except Exception as e:
    print('Token is invalid! Add your bot token to config.json.')