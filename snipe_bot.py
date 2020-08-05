# Usage -<track/untrack> <CRN>

import discord
from oscar_scraper import *
from discord.ext import commands
import requests

def add_class(user, crn):
    if user in trackers.keys():
        if crn not in trackers[user]:
            trackers[user].append(crn)
    else:
        trackers[user] = [crn]

def remove_class(user, crn):
    trackers[user].remove(crn)

trackers = {}

client = commands.Bot(command_prefix='$')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def track(ctx, crn):
    try:
        status = class_status(scrape(crn))
        add_class(ctx.author.id, crn)
        await ctx.send(f'{ctx.author.mention} Now tracking {crn}.')
    except:
        await ctx.send(f'{ctx.author.mention} Could not find class with CRN: {crn}.')


@client.command()
async def untrack(ctx, crn):
    user_tracks = trackers.get(ctx.author.id)
    if user_tracks and crn in user_tracks:
        remove_class(ctx.author.id, crn)
        await ctx.send(f'{ctx.author.mention} Stopped tracking {crn}.')
    else:
        await ctx.send(f'{ctx.author.mention} You are not tracking {crn}. Did you mean "track"?')


client.run('NzQwNTAxNDA2NzE2Mzk1NjAw.Xyp7rQ.VhoKExn-j8EdvpB3OsnQZgWY0VQ')

class ClassStatus():
    def __init__(self, crn, status):
        self.crn = crn
        self.status = status

    