import discord
from discord.ext import commands
from discord.ext.commands import Bot

import asyncio
import time
import random
import os
import sys
import json
import datetime
import traceback
import logging

TOKEN = 'MTAyMDY2NzMwNTIyODc2NzM1Mw.GWVcQe.vMImOqr_xwsFI0ik10EspSWjhIfu1dtIempq2k'

einladung = 'test'

hilfe = ''

bot = commands.Bot(command_prefix='!') 

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

async def on_message(message):
    if message.content.startswith('!discord'):
        await bot.send_message(message.channel, einladung)
    if message.content.startswith('!help'):
        await bot.send_message(message.channel, hilfe)
    

bot.run(TOKEN, bot=True, reconnect=True)