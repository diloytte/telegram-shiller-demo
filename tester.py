from telethon.sync import TelegramClient;
from datetime import date
from group_ids import group_ids_1, group_ids_2, group_ids_3, test_group_id, archivable_chats, priority_groups
from shills import get_shill_by_index
import os
from telethon.tl.types import PeerChannel
from telethon.errors import ChannelInvalidError, ChannelPrivateError
from telethon.tl.functions.channels import GetFullChannelRequest
from groups_dictionary import group_name_to_id

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

async def check_membership(group_id, group_name_to_id):
    group_name = next((name for name, id in group_name_to_id.items() if id == group_id), None)
    if group_name is None:
        return "Unknown Group", "Group not found"

    print(f"Checking {group_name} ({group_id})")
    try:
        await client(GetFullChannelRequest(group_id))
        return group_name, "YES IN"
    except ChannelPrivateError:
        return group_name, "NO not in (left_or_private)"
    except ChannelInvalidError:
        return group_name, "NO not in (invalid_id)"
    except Exception as e:
        return group_name, f"error: {str(e)}"

async def check_all_groups_membership(group_ids, group_name_to_id):
    results = {}
    output_lines = []
    output_lines.append(f"{'Group Name':<20} {'Group ID':<15} {'Status':<30}")
    output_lines.append("-" * 65)

    for group_id in group_ids:
        group_name, status = await check_membership(group_id, group_name_to_id)
        group_name_display = group_name if group_name != "Unknown Group" else "Unknown (Not Found)"
        output_lines.append(f"{group_name_display:<20} {str(group_id):<15} {status:<30}")
        results[group_id] = (group_name, status)

    print("\n".join(output_lines))
    return results

async def print_dialogs():
    dialogs = await client.get_dialogs()
    value = -1
    for dialog in dialogs:
        # print(f"Name:{dialog.name}  ID: {dialog.id},  TYPE: {type(dialog.entity).__name__}")
        if "40" in dialog.name:
            print(dialog.id)
            print(dialog.name)

# vidi dal u dialogima koje si zapisao idalje ih imas.. vrati neki imo o njima.. dodaj 4tix

async def send_message(id,message):
    await client.send_message(id,message)

async def shill(ca,shill_index):
    for group in priority_groups:
        # await send_message(group,"D1TK6G8fcrW3wdrQd914YxhEeVKvbHLZz11YqUrTpump\n\n news based event, i think it has potential to go viral. dyor")
        await send_message(group,get_shill_by_index(ca,shill_index))

async def run():
    await client.connect()
    # await print_dialogs()
    # await check_all_groups_membership(priority_groups,group_name_to_id)
    # await send_message(-1002014016057,"/")
    await shill("CA",6) 
    # await archive_all_archivable()

if __name__ == "__main__":
    with client:
        client.loop.run_until_complete(run())



        