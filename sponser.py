import asyncio
import time
from pyrogram import filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message          
from config import OWNER_ID
from pandora import app, userbot
from pandora.utils.database import (get_served_chats, get_served_users)
from pandora.promo import (promo_photo, promo_text)

p_banner = promo_photo
p_text = promo_text


@app.on_message(filters.command("arnavtc") & filters.user(OWNER_ID))
async def sponsership(client, message: Message, _):
	loaded_chats = []
	load_db_chats = await get_served_chats()
	loaded_users = []
	load_db_users = await get_served_users()


	sent_togp=0
	sent_usr=0
	for getchats in load_db_chats:
		loaded_chats.append(int(getchats["chat_id"]))

	await asyncio.sleep(30)
	for sexyusers in load_db_users:
		loaded_users.append(int(sexyusers["user_id"]))

	await asyncio.sleep(10)
	countingsex = int(len(loaded_chats))
	countingusers = int(len(loaded_users))
	try:
		await message.reply_text(f"<b>{countingsex}</b> chats & <b>{countingusers}</b> users loaded ✅\nBroadcast started now...🚀")
	except:
		print(f"{countingsex} Chats Loaded!")

	for cht_id in loaded_chats:
		try:
			await app.send_photo(cht_id, p_banner, caption=p_text)
			sent_togp+=1

		except FloodWait as e:
			flood_wtime = int(e.x)
			if flood_wtime > 200:
				continue 
			await asyncio.sleep(flood_wtime)
	try:
		await message.reply_text(f"**Broadcasted Message In {sent_togp} Chats.✅**")
	except:
		print(f"**Bot Failed To Send Reporting To Command Place!\nTotal {sent_togp} Recived the broadcasting message!")

	for useridlol in loaded_users:
		try:
			await app.send_photo(useridlol, p_banner, caption=p_text)
			sent_usr+=1
		except FloodWait as e:
			flood_wtime = int(e.x)
			if flood_wtime > 200:
				continue
			await asyncio.sleep(flood_wtime)
	try:
		await message.reply_text(f"**Broadcasted Message To {sent_usr} Users.✅**")

	except:
		print(f"**Bot Failed To Send Reporting To Command Place!\nTotal {sent_usr} Users Recived the broadcasting message!")

