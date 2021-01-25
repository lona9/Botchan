import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from discord.utils import get
import datetime
from datetime import datetime
import random
import asyncio
import pendulum
from keep_alive import keep_alive 

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="&")

#RELOJITO
@bot.command()
async def hora(ctx):
# TIMEZONES
  tz_CL = pendulum.timezone('America/Santiago')
  datetime_CL = datetime.now(tz_CL)

  tz_PE = pendulum.timezone('America/Lima')
  datetime_PE = datetime.now(tz_PE)

  tz_BO = pendulum.timezone('America/La_Paz')
  datetime_BO = datetime.now(tz_BO)

  tz_JP = pendulum.timezone('Asia/Tokyo')
  datetime_JP = datetime.now(tz_JP)

  tz_MX = pendulum.timezone('America/Mexico_City')
  datetime_MX = datetime.now(tz_MX)

  hora = ("La hora actual es:", "\n", ":flag_mx: (CDMX) **(GMT -6): **", datetime_MX.strftime("%H:%M:%S"), "\n", ":flag_pe: :flag_ec: :flag_co: **(GMT -5): **", datetime_PE.strftime("%H:%M:%S"), "\n", ":flag_bo: :flag_py: :flag_ve: **(GMT -4): **", datetime_BO.strftime("%H:%M:%S"), "\n", ":flag_ar: :flag_cl: :flag_br: :flag_uy: **(GMT -3) : **", datetime_CL.strftime("%H:%M:%S"), "\n", ":flag_kr: :flag_jp: **(GMT +9): **", datetime_JP.strftime("%H:%M:%S"))

  await ctx.channel.send("".join(hora))


#TRIGGERS 
@bot.event
async def on_message(message):
  if message.author == bot.user:
    return

  msg = message.content

#EASTER EGGS
  if 'hola' in msg.lower():
    await message.channel.send('Hola!')

  await bot.process_commands(message)

keep_alive()

bot.run(DISCORD_TOKEN)