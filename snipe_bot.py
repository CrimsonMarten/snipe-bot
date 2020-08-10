# Usage -<track/untrack> <CRN>

import discord
from oscar_scraper import *
from discord.ext import commands
import requests

def add_class(user, crn):
    """
    Precondition: crn is validated
    """ 
    if crn in tracking and user not in tracking[crn]:
        tracking[crn].append(user)
    else:
        tracking[crn] = [user]
    

def remove_class(user, crn):
    tracking[crn].remove(user)

tracking = {}
class_status = {}

client = commands.Bot(command_prefix='$')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def track(ctx, crn):
    try:
        status = class_status(scrape(crn))
        add_class(ctx.author.id, crn)
        class_status[crn] = status
        await ctx.send(f'{ctx.author.mention} Now tracking {crn}.')
    except:
        await ctx.send(f'{ctx.author.mention} Could not find class with CRN: {crn}.')


@client.command()
async def untrack(ctx, crn):
    if crn in tracking and ctx.author.id in tracking[crn]:
        remove_class(ctx.author.id, crn)
        await ctx.send(f'{ctx.author.mention} Stopped tracking {crn}.')
    else:
        await ctx.send(f'{ctx.author.mention} You are not tracking {crn}. Did you mean "track"?')

def check_for_status_changes():
    changed_status = []
    for crn in tracking:
        status = class_status(scrape(crn))
        if status != class_status[crn]:
            changed_status.append(crn)
            class_status[crn] = status
    return changed_status

def notify():
    

client.run('your-token-here')

    