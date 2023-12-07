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
  current_time = datetime.datetime.now(pytz.timezone('Asia/Ho_Chi_Minh'))
  await channel.send(f'ON AIR! {current_time}')
  change_nickname.start()
  change_channel_name.start()

@tasks.loop(time = datetime.time(hour = 0, minute = 0, tzinfo = pytz.timezone('Asia/Ho_Chi_Minh')))
async def change_nickname():
  guild = client.get_guild(1053081261394116778)
  member = guild.get_member(920722041542426687)
  current_time = datetime.datetime.now(pytz.timezone('Asia/Ho_Chi_Minh'))
  target_date = datetime.datetime(2024, 2, 10, tzinfo=pytz.timezone('Asia/Ho_Chi_Minh'))
  remaining_days = (target_date - current_time).days + 1
  if (remaining_days > 0):
    await member.edit(nick = f'{remaining_days} ngày nữa là Tết')
  else: 
    await member.edit(nick = 'Happy New Year!!!')

@tasks.loop(minutes = 11)
async def change_channel_name():
  guild = client.get_guild(1053081261394116778)
  channel = guild.get_channel(1178870060866085034)
  bot = guild.get_member(889043536555687936)
  
  current_time = datetime.datetime.now(pytz.timezone('Asia/Ho_Chi_Minh'))
  target_date = datetime.datetime(2023, 12, 24, tzinfo=pytz.timezone('Asia/Ho_Chi_Minh'))
  remaining_days = target_date - current_time
  remaining_seconds = remaining_days.days * 24 * 3600 + remaining_days.seconds 
  
  days = remaining_seconds // (24 * 3600) 
  
  remaining_seconds = remaining_seconds % (24 * 3600) 
  hours = remaining_seconds // 3600
  
  remaining_seconds %= 3600
  minutes = remaining_seconds // 60

  await channel.edit(name = f'{days}D {hours}H {minutes}M to Noel')
  await bot.edit(nick = f'{days}D to Noel')
  
intents = discord.Intents.default()
intents.message_content = True

client.run(os.environ['DISCORD_TOKEN'])
