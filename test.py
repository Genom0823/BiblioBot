# python3

import discord
from datetime import datetime
import sqlite3

import cogs

#dbname = 'TEST.db'
#conn = sqlite3.connect(dbname)

#cur = conn.cursor()
#cur.execute('CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)')
#name = "Taro"
#cur.execute(f'INSERT INTO persons(name) values(:name)', {"name": name})
#conn.commit()

#conn.close()

# find book info
book_info = cogs.bookshelf.get_book_info('9784046821461', cogs.bookshelf.BookData.DESCRIPTION)
print(book_info)

'''
url = 'https://hon-hikidashi.jp/tag/line-up/'

articles = cogs.url.get_elements_by_class(url, 'detail__ttl')
top_article = articles[0].contents[0].get('href')

res = cogs.url.get_elements_by_tag(top_article, 'tr')

for r in res:
    print(list(r.stripped_strings))

#print(res[4])
'''
#
'''
intents = discord.Intents.all()
intents.message_content = True
client = discord.Client(intents = intents)

@client.event
async def on_ready():

    await client.wait_until_ready()
    print('起動しました')


@client.event
async def on_voice_state_update(member, before, after):

    if (before.channel != after.channel) and (member.status == discord.Status.online):
        
        # get guild
        notify_guild = member.guild
        # get notify channel
        notify_channel = discord.utils.get(notify_guild.text_channels, name="vc-notify")
        
        if after.channel != None:

            text = f"{member.name} が 『{after.channel}』 に入室しました"

            if member.id == 873217212842913812:
                text = f"{member.name} が 『{after.channel}』 に入ってきやがった。はよ出て行けや。"

            notify_embed = discord.Embed(
                title="入室通知", 
                color=0xabdab5, 
                description=text, 
                timestamp=datetime.now()
                )
            
            print(f"{member.id}")
            notify_embed.set_thumbnail(url=member.avatar)

        elif after.channel == None:

            text = f"{member.name} が 『{before.channel}』 から退室しました"

            if member.id == 873217212842913812:
                text = f"{member.name} が 『{before.channel}』 から出ていった。一生入ってくんな。"

            notify_embed = discord.Embed(
                title="退室通知", 
                color=0xf28b82, 
                description=text, 
                timestamp=datetime.now()
                )
            
            notify_embed.set_thumbnail(url=member.avatar)

        
        await notify_channel.send(embed = notify_embed)


@client.event
async def on_guild_join(guild):

    notify_channel = discord.utils.get(guild.text_channels, name="vc-notify")

    
    # create notify channel
    if notify_channel == None:
        notify_category = await guild.create_category("Notify")
        notify_channel = await guild.create_text_channel("vc-notify", category = notify_category)


@client.event
async def on_presence_update(before, after):

    if after.activity != None:
        activity_guild = after.guild
        activity_channel = discord.utils.get(activity_guild.text_channels, name="vc-notify")
        print(f'{after.guild}:{after.activity.name}')


client.run(TOKEN)
'''