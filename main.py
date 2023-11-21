import discord
from discord.ext import tasks, commands
import os

from datetime import datetime, timedelta
import pytz

target_date = datetime(2024, 2, 10, tzinfo=pytz.timezone('Asia/Ho_Chi_Minh'))
current_date = datetime.now(pytz.timezone('Asia/Ho_Chi_Minh'))

remaining_days = (target_date - current_date).days #int
# print(f"Remaining days until {target_date.date()}: {remaining_days}")


client = commands.Bot(command_prefix='$', intents = discord.Intents.all())

intents = discord.Intents.all()
intents.message_content = True
# client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print(f"log in as {client.user}: {client.user.id}")
  someloop.start()


@tasks.loop(seconds=1)
async def someloop():
  # member=client.get_member(920722041542426687)
  guild = client.get_guild(1053081261394116778)
  member = guild.get_member(920722041542426687)
  target_date = datetime(2024, 2, 10, tzinfo=pytz.timezone('Asia/Ho_Chi_Minh'))
  current_date = datetime.now(pytz.timezone('Asia/Ho_Chi_Minh'))

  remaining_days = (target_date - current_date).days
  await member.edit(nick=str(remaining_days))
  
# @client.command()
# async def chnick(ctx, nick):
#     member = ctx.guild.get_member(member_id)
#     if member:
#         await member.edit(nick=nick)
#         await ctx.send(f'Nickname was changed for {member.mention} ')
#     else:
#         await ctx.send("Member not found")
# @client.listen()
# async def on_ready():
#   change_nickname.start() ########################################################
  
# count = 1
# @tasks.loop(seconds=10)  # Run every 24 hours
# async def change_nickname():
#     # target_date = datetime(2024, 2, 10, tzinfo=pytz.timezone('Asia/Ho_Chi_Minh'))
#     # current_date = datetime.now(pytz.timezone('Asia/Ho_Chi_Minh'))

#     # if current_date.date() == target_date.date():
#     #     member = guild.get_member(member_id)
#     #     if member:
#     #         new_nickname = "NewNickname"  # Set the new nickname here
#     #         await member.edit(nick=new_nickname)
#   member = guild.get_member(member_id)
#   new_nickname = "{count}" # Set the new nickname here
#   count=count+1
#   await member.edit(nick=new_nickname)


intents = discord.Intents.default()
intents.message_content = True

client.run(os.environ['discord_token'])