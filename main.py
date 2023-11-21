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
  someloop.start()

time = datetime.time(hour = 0, minute = 0,tzinfo = pytz.timezone('Asia/Ho_Chi_Minh'))

@tasks.loop(time = time)
async def someloop():
  guild = client.get_guild(1053081261394116778)
  member = guild.get_member(920722041542426687)
  target_date = datetime.datetime(2024, 2, 10, tzinfo=pytz.timezone('Asia/Ho_Chi_Minh'))
  current_date = datetime.datetime.now(pytz.timezone('Asia/Ho_Chi_Minh'))
  remaining_days = (target_date - current_date).days
  await member.edit(nick = f'{remaining_days} ngày nữa là Tết')

intents = discord.Intents.default()
intents.message_content = True

client.run(os.environ['discord_token'])