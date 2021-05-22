from discord.ext import commands
import asyncio
import os
from poc import *
import requests

prefix = "!"
bot = commands.Bot(command_prefix=prefix)


@bot.event
async def on_ready():
    print("Logged in.")
    bot.webhooks = {}


@bot.event
async def on_message(message):
    await bot.process_commands(message)


@bot.command()
async def ping(ctx):
    '''
    Bot ping
    '''
    await ctx.send(bot.latency)

@bot.command()
async def setup(ctx):
    if not ctx.author.guild_permissions.administrator:
        await ctx.send("This command MUST be run as admin.")
    await ctx.send("Removing Old Webhooks...")
    hooks = await ctx.channel.webhooks()
    for h in hooks:
        await h.delete(reason="Removing Old Webhooks")
        await asyncio.sleep(2)
    await ctx.send("Creating New Webhooks!")
    for i in range(0, 10):
        x = await ctx.channel.create_webhook(name=f"{i+1}")
        bot.webhooks[i] = x
        await asyncio.sleep(5)
    await ctx.send("Done! You can use the `run_hook` command to run the animation now!")


@bot.command()
async def run(ctx):
    print("===Bad Apple in Discord===")
    print("===By NateM135===")
    await ctx.send("Loading all data...")
    with open('output.json') as json_file:
        data = json.load(json_file)
    await asyncio.sleep(1)
    await ctx.send("=========\nStarting in 3 Seconds")
    await asyncio.sleep(3)
    for frame in data:
        await ctx.send("```" + data[frame] + "```")
        print(f"Rendered {frame}/{len(data)}.")
        await asyncio.sleep(2)
    


@bot.command()
async def run_hook(ctx):
    sample_data = test()
    b = False
    for f in range(40, 100, 2):
        if b:
            ind = f%10
        else:
            ind = f%10+1
        await webhook(bot.webhooks[ind].url,"```"+sample_data[f]+"```")
        await sleep()
        if(f%10==0):
            b= not b
        print(bot.webhooks[ind].url)
        # print(f"{f%10}:{f}")
        #await asyncio.sleep(.1)
        #await ctx.channel.send("```"+sample_data[f]+"```")
        #await asyncio.sleep(1)

async def webhook(url, content):
    #for all params, see https://discordapp.com/developers/docs/resources/webhook#execute-webhook
    data = {
        "content" : content,
        "username" : "custom username"
    }

    result = requests.post(url, json = data)

    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)

async def sleep():
    await asyncio.sleep(.2)

def main():
    for i in range(0, 100):
        print("a")
        asyncio.run(webhook("a"))
        asyncio.run(sleep())

bot.run("PUT YOUR TOKEN HERE! IMAGINE USING ENVIRONMENT VARIABLES")