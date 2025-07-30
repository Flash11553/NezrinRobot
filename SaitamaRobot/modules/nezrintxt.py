import secrets
import string
import aiohttp
from pyrogram import filters
from cryptography.fernet import Fernet
from SaitamaRobot import pbot
from AykhanPro.komekci import random_line


@pbot.on_message(filters.command("meslehet"))
async def meslehet(_, message):
    await message.reply_text((await random_line('AykhanPro/txt/meslehet.txt')))


@pbot.on_message(filters.command("anekdod"))
async def anekdod(_, message):
    await message.reply_text((await random_line('AykhanPro/txt/anekdod.txt')))

