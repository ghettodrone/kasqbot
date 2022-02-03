import discord, asyncio, time
from discord.ext import commands
from discord import Game
from discord.ext.commands import Bot
from itertools import cycle
import random 
import ctypes
import json
import os
import re
from datetime import datetime
from discord.utils import get




Bot = commands.Bot(command_prefix= '?')


status = ['за KASQ','Порно', '?help']

@Bot.event
async def on_ready():
    print("Ботик на месте йоу")
    print("--------------------")
    print('Logged in as')
    print("--------------------")
    print(Bot.user.name)
    print("--------------------")
    print(Bot.user.id)
    print('--------------------')

    while True:
        for i in status:
            await Bot.change_presence(status= discord.Status.dnd, activity=discord.Activity(name= i, type=discord.ActivityType.watching))
            await asyncio.sleep(10)


@Bot.event
async def on_member_join(member):
    channel = Bot.get_channel(9358388326733045979) 
    role_id = 605056528323706891
    role = get(member.guild.roles, id=role_id)
    emb = discord.Embed(title= "Здарова!,** {} **".format(member.name), description= "Советую, заглянуть в канал {#правила}.\n Чтобы получить рольку, которая тебе по душе зайди в {#roles}. ", color= 0x3600ff)
    emb.set_author(name= "KASQ" , icon_url= 'https://cdn.discordapp.com/avatars/610551362161344522/c3186aab6fae251f92262fd9b958d51b.webp?size=1024')
    emb.set_image(url= 'https://cdn.discordapp.com/attachments/605056149925920778/662600096352829440/8003416_184013fb.gif')
    emb.set_footer(text= 'ID: {}'.format(member.id), icon_url= member.avatar_url)
    await member.add_roles(role)
    await channel.send(embed= emb) 
    



Bot.run('NjEwNTUxMzYyMTYxMzQ0NTIy.XVG6RA.Bxp6r6Syy251mkCiBAwG2h6L5dc')
