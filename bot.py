# python3

from datetime import datetime
import sqlite3

import discord
from discord import app_commands

import setup
from cogs import bookshelf as bookshelf


# Set up discord client
intents = discord.Intents.all()
intents.message_content = True
client = discord.Client(intents = intents)

# Set Command tree
tree = app_commands.CommandTree(client)
# Bot Token
TOKEN = setup.TOKEN


@client.event
async def on_ready():
    await client.wait_until_ready()
    await tree.sync()
    print('起動しました')


@client.event
async def on_guild_join(guild):
    notify_channel = discord.utils.get(guild.text_channels, name="vc-notify")

    # create notify channel
    if notify_channel == None:
        notify_category = await guild.create_category("Notify")
        notify_channel = await guild.create_text_channel("vc-notify", category = notify_category)


@tree.command(name="isbn",description="ISBNコードから書籍情報を検索します")
async def info_from_isbn(
    interaction: discord.Interaction,
    isbn:str,
    data:bookshelf.BookData):
    info = bookshelf.get_book_info(isbn, data)

    if info == None:
        info = '書籍情報が見つかりませんでした'

    await interaction.response.send_message(f'書籍情報が見つかりました \n ISBN:{isbn} \n {info}',ephemeral=False)


client.run(TOKEN)