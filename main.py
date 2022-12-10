import random

import discord

import re

import sqlite3

from datetime import datetime  # reference to the class instead of just the module

from table2ascii import table2ascii, PresetStyle

intents = discord.Intents.default()
intents.message_content = True

class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):

        args = message.content.split()


client = MyClient(intents=intents)
with open('token.txt') as f:
    content = f.read()
client.run(content)