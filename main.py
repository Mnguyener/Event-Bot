import random

import discord

import re

import sqlite3

from datetime import datetime  # reference to the class instead of just the module

from table2ascii import table2ascii, PresetStyle

intents = discord.Intents.default()
intents.message_content = True

con = sqlite3.connect("messages.db")
cur = con.cursor()
print("Connected to SQLite")
cur.execute("""CREATE TABLE IF NOT EXISTS polls (creator INTEGER NOT NULL, time DATETIME, msg TEXT)""")

def christmas_poll(_creator, _time, _msg) -> "list":
    try:
        cur.execute("""INSERT into polls (creator, time, msg) VALUES  (?,?,?)""",
                    [_creator,_time,_msg])
        con.commit()
        print("date added")
    except sqlite3.Error as error:
        print(error)
class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        args = message.content.split()

        if args[0] == "$poll":
            if len(args) == 1:
                await message.reply("Not enough arguments!")
            elif args[1] == "16" or args[1] == "26":
                my_embed = discord.Embed(title="Secret Santa Gathering",
                                         description="Vote on which days you guys are available!",
                                         colour=0x228B22)
                my_embed.set_thumbnail(
                    url="https://www.history.com/.image/t_share/MTY4ODE4ODA4MzY1MDAwNDY1/christmas-gettyimages-184652817.jpg")
                msg = args[1]
                creator = str(message.author.id)
                time = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
                christmas_poll(creator, time, msg)
                my_embed.add_field(name="Possible Dates", value="🅰️ Dec 16th\n\n 🅱️ Dec 26th\n", inline=True)
                await message.reply(embed=my_embed)

            else:
                await message.reply("Error.")
client = MyClient(intents=intents)
with open('token.txt') as f:
    content = f.read()
client.run(content)
