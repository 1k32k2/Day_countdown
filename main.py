import os
import logging
from datetime import datetime, time

import discord
from discord.ext import tasks, commands
import pytz

from countdown import (
  now_in_tz,
  remaining_days_inclusive,
  remaining_dhm,
  TIMEZONE,
)

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

# Config - prefer environment variables for IDs and dates so behaviour can be changed
GUILD_ID = int(os.getenv('DC_GUILD_ID', '1053081261394116778'))
NICK_MEMBER_ID = int(os.getenv('DC_MEMBER_ID', '920722041542426687'))
CHANNEL_ID = int(os.getenv('DC_CHANNEL_ID', '1455907549332373670'))

# Target dates can be supplied via env using ISO format, fallback to previous hard-coded values
def parse_iso_date(env_name: str, default: str) -> datetime:
  val = os.getenv(env_name)
  tz = pytz.timezone(TIMEZONE)
  if not val:
    # default is YYYY-MM-DD or YYYY-MM-DDTHH:MM
    return datetime.fromisoformat(default).replace(tzinfo=tz)
  # allow ISO with or without time
  return datetime.fromisoformat(val).replace(tzinfo=tz)

NICK_TARGET_DATE = parse_iso_date('DC_NICK_TARGET', '2026-02-17')
CHAN_TARGET_DATE = parse_iso_date('DC_CHAN_TARGET', '2026-02-17')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = commands.Bot(command_prefix='$', intents=intents)


@client.event
async def on_ready():
  log.info("Logged in as %s (id=%s)", client.user, client.user.id)
  # send a startup message if the (optional) channel is available
  channel = client.get_channel(1053585169182896228)
  try:
    current_time = now_in_tz()
    if channel:
      await channel.send(f'ON AIR! {current_time}')
  except Exception:
    log.exception("Failed to send startup message")

  # start background tasks
  if not change_nickname.is_running():
    change_nickname.start()
  if not change_channel_name.is_running():
    change_channel_name.start()


@tasks.loop(time=time(hour=0, minute=0, tzinfo=pytz.timezone(TIMEZONE)))
async def change_nickname():
  guild = client.get_guild(GUILD_ID)
  if not guild:
    log.warning("Guild %s not found in cache", GUILD_ID)
    return

  member = guild.get_member(NICK_MEMBER_ID)
  if not member:
    log.warning("Member %s not found in guild %s", NICK_MEMBER_ID, GUILD_ID)
    return

  current_time = now_in_tz()
  remaining_days = remaining_days_inclusive(NICK_TARGET_DATE, current_time)
  try:
    if remaining_days > 0:
      await member.edit(nick=f'{remaining_days} ngày nữa là Tết')
    else:
      await member.edit(nick='Happy New Year!!!')
  except Exception:
    log.exception("Failed to change nickname for member %s", NICK_MEMBER_ID)


@tasks.loop(minutes=3)
async def change_channel_name():
  guild = client.get_guild(GUILD_ID)
  if not guild:
    log.warning("Guild %s not found in cache", GUILD_ID)
    return

  channel = guild.get_channel(CHANNEL_ID)
  if not channel:
    log.warning("Channel %s not found in guild %s", CHANNEL_ID, GUILD_ID)
    return

  current_time = now_in_tz()
  days, hours, minutes = remaining_dhm(CHAN_TARGET_DATE, current_time)
  try:
    await channel.edit(name=f'{days}D {hours}H {minutes}M to Tết')
  except Exception:
    log.exception("Failed to edit channel name %s", CHANNEL_ID)


token = os.getenv('DISCORD_TOKEN')
if not token:
  log.error('DISCORD_TOKEN environment variable not set. Exiting.')
else:
  client.run(token)