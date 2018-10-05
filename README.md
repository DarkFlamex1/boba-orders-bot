# Boba Orders Bot
boba-orders-bot is a discord bot that gives users a list of boba drinks to choose from, as well as some other parameters (sweetness, size, etc.)

## Planned Features
1. There must be a command so that users may see what flavors of boba they  can order
1. Users must be able to send the bot a request for a specific boba flavor with specific parameters (one may have their own syntax for taking this input in)
1. The bot must store all the boba orders in some way
1. Users with certain roles can clear the list
1. Users can request their order to see what they have ordered so far

## Installation
boba-orders-bot works with the [discord.py](https://github.com/Rapptz/discord.py/tree/rewrite) module. 

**IMPORTANT:** You must install the `discord.py` rewrite! 

To install the rewrite version in one step:
`python3 -m pip install -U https://github.com/Rapptz/discord.py/archive/rewrite.zip#egg=discord.py[voice]`

Or the long way around:
1. `git clone https://github.com/Rapptz/discord.py/`
2. `cd discord.py`
3. `git checkout rewrite`
4. `python3 -m pip install -U .[voice]`

## Run bot
1. View basic Discord bot setup instructions [here](https://discordpy.readthedocs.io/en/rewrite/discord.html).
2. Copy your token to `token.json`.
3. Run the bot using `python3 bot.py`.

## Contributors
 - [Muaaz Wahid](https://github.com/MuaazWahid)
 - [Ben Cuan](https://github.com/dbqeo)

Image credits: http://anothersunday.me/blog/2015/8/29/vegan-bubble-almond-milk-tea
