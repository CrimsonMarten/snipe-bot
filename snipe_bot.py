# Usage -<track/untrack> <CRN>

import discord
from discord.ext import commands

trackers = {}

client = commands.Bot(command_prefix='$')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def track(ctx, crn):
    await ctx.send(f'{ctx.author.mention} Now tracking {crn}.')

@client.command()
async def untrack(ctx, crn):
    user_tracks = trackers.get(ctx.author)
    if user_tracks and crn in user_tracks:
        remove_class(ctx.author, crn)
        await ctx.send(f'{ctx.author.mention} Stopped tracking {crn}.')
    else:
        await ctx.send(f'{ctx.author.mention} You are not tracking {crn}. Did you mean "track"?')

client.run('NzQwNTAxNDA2NzE2Mzk1NjAw.Xyp7rQ.WmmZ5fRVMsJX90sVY4zvcT59B5k')

def add_class(user, crn):
    if user in trackers:
        if crn not in trackers[user]:
            trackers[user].append(crn)
    else:
        trackers[user] = [crn]

def remove_class(user, crn):
    trackers[user].remove(crn)