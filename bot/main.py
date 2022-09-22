import discord
import asyncio



TOKEN = 'MTAyMDY2NzMwNTIyODc2NzM1Mw.GWVcQe.vMImOqr_xwsFI0ik10EspSWjhIfu1dtIempq2k'

einladung = 'test'

Client = discord.Client()

hilfe = ''

@Client.event
async def on_ready():
    print('Logged in as')
    print(Client.user.name)
    print(Client.user.id)
    print('------')

async def on_message(message):
    if message.content.startswith('!discord'):
        await Client.send_message(message.channel, einladung)
    if message.content.startswith('!help'):
        await Client.send_message(message.channel, hilfe)

Client.run(TOKEN)