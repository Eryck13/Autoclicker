import discord
from discord.ext import commands,tasks
import datetime
from discord.ext.commands import has_permissions, MissingPermissions, CheckFailure
import asyncio
import os
from seleniumwire import webdriver
import json

path=os.path.dirname(os.path.abspath(__file__))
with open(path+'\\config.txt','r') as f:
    config = json.load(f)
    channel = config['Channel']
    token = config["Token"]
    linkkw = config["LinkKeyword"]
    linkkw = linkkw.lower()

client = commands.Bot(command_prefix='!')
driver = webdriver.Chrome(path+"\\chromedriver.exe")
driver.get("https://www.boringbot.io")

@client.event
async def on_ready():
    print ('ready') 

@client.event
async def on_message(message):
    try:
        await client.process_commands(message)
        Channelfrom =  client.get_channel(int(channel))
        
        if message.channel.id == Channelfrom.id:
            if message.content == '':
                embed=message.embeds[0]
                try:
                    fields = embed.fields
                    desc = embed.description
                    if 'http' and linkkw in desc.lower():
                        find = desc.split(" ")
                        for i in find:
                            if 'http' and linkkw in i.lower():
                                link = i
                                driver.get(link)
                    
                    for each in fields:
                        contents = each.value
                        if 'http' and linkkw in contents.lower():
                            find = contents.split(" ")
                            for i in find:
                                if 'http' and linkkw in i.lower():
                                    link = i
                                    driver.get(link)
                        else:
                            pass
                except:
                    pass        
            
            elif "http" and linkkw in message.content.lower():
                try:
                    find2 = message.content
                    link2 = find2.split(" ")
                    for each in link2:
                            if 'http' and linkkw in each.lower():
                                link = each
                                driver.get(link)
                            else:
                                pass
                except:
                    pass
    except:
        pass

client.run(token)