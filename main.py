import discord
from discord.ext import tasks, commands
import os
import datetime
import pytz

client = commands.Bot(command_prefix='$', intents = discord.Intents.all())
intents = discord.Intents.all()
intents.message_content = True

@client.event
async def on_ready():
  print(f"log in as {client.user}: {client.user.id}")
  channel = client.get_channel(1053585169182896228)
  # await channel.send('ON AIR!')
  # change_nickname.start()
  change_channel_name.start()

time = datetime.time(hour = 0, minute = 0, tzinfo = pytz.timezone('Asia/Ho_Chi_Minh'))

# @tasks.loop(time = time)
# async def change_nickname():
#   guild = client.get_guild(1053081261394116778)
#   member = guild.get_member(920722041542426687)
#   target_date = datetime.datetime(2024, 2, 10, tzinfo=pytz.timezone('Asia/Ho_Chi_Minh'))
#   current_date = datetime.datetime.now(pytz.timezone('Asia/Ho_Chi_Minh'))
#   remaining_days = (target_date - current_date).days + 1
#   if (remaining_days > 0):
#     await member.edit(nick = f'{remaining_days} ngày nữa là Tết')
#   else: 
#     await member.edit(nick = 'Happy New Year!!!')

@tasks.loop()
async def change_channel_name():
  guild = client.get_guild(1053081261394116778)
  channel = guild.get_channel(1178870060866085034)
  target_date = datetime.datetime(2023, 12, 24, tzinfo=pytz.timezone('Asia/Ho_Chi_Minh'))
  current_date = datetime.datetime.now(pytz.timezone('Asia/Ho_Chi_Minh'))
  remaining_days = target_date - current_date
  print(remaining_days)
  # await channel.edit(name = 'ewkjrhgjgh')

intents = discord.Intents.default()
intents.message_content = True

client.run(os.environ['discord_token'])