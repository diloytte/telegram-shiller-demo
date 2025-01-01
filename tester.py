from telethon.sync import TelegramClient;
from datetime import date
from group_ids import group_ids_1, group_ids_2, group_ids_3, test_group_id, archivable_chats
from shills import get_shill_random, get_shill_by_index
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path='.env')

session_name = os.getenv('SESSION_NAME')
api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")

client = TelegramClient(session_name,api_id,api_hash)
all_groups = group_ids_1 + group_ids_2 + group_ids_3


async def archive_all_archivable():
    for chat in archivable_chats:
        await archive_chat(chat)

async def archive_chat(id):
    await client.edit_folder(id,1)

async def print_dialogs():
    dialogs = await client.get_dialogs()
    for dialog in dialogs:
        # print(f"Name:{dialog.name}  ID: {dialog.id},  TYPE: {type(dialog.entity).__name__}")
        if "lynk" in dialog.name:
            print(dialog.id)

async def send_message(id,message):
    await client.send_message(id,message)

async def shill(CA):
    for group in all_groups:
        await send_message(group,get_shill_by_index("CA",1))

async def run():
    await client.connect()

    await shill("CA") 
    await archive_all_archivable()

if __name__ == "__main__":
    with client:
        client.loop.run_until_complete(run())



        