import sys
import datetime

from os import execle, environ
from config import SUDO_USERS

from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["ping"], ["/", ".", "!"]))
async def ping(_, e: Message):       
      start = datetime.datetime.now()
      Fuk = await e.reply("⚡")
      end = datetime.datetime.now()
      ms = (end-start).microseconds / 1000
      await Fuk.edit_text(f"ꜱ ᴛ ᴏ ʀ ᴍ 🥀\nᴛʜᴇ ᴄᴀʟᴍ ʙᴇꜰᴏʀᴇ ᴛʜᴇ ꜱᴛᴏʀᴍ ⚡\n» `{ms} ᴍꜱ`")