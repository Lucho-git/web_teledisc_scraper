#Initializations

import sys
import asyncio   #desyncs telegram calls to make timings work, idk
import nest_asyncio          #this should only be needed when using, google colabs or other webbased stuff, I think its because these sites run in a coding loop or are different from regular env
import telethon.sync
#import telebot             #import telegram bot library
import requests

from telethon import TelegramClient, events
from telethon.sync import TelegramClient
from telethon.tl.types import (PeerChannel)
from telethon import functions, types
from telethon.sessions import StringSession

async def first_log_in(phone, api_id, api_hash):
    client = TelegramClient(phone, api_id, api_hash)
    await client.connect()  
    print("Client Connected")

    if not await client.is_user_authorized():
      await client.send_code_request(phone)
      print("Sending Code")
      try:
        await client.sign_in(phone, input('Enter the code: '))
      except Exception as e:
        print(e)
    else:
      print("Client Authorized ....")
    stringsesh = StringSession.save(client.session)
    print("Saving Session")
    await client.disconnect()
    print("Disconnecting\n")
      
    return stringsesh



def main_loop()
  nest_asyncio.apply()
  loop = asyncio.get_event_loop()
  stringsesh = None
  api_id = '5747368'
  api_hash = '19f6d3c9d8d4e6540bce79c3b9223fbe'
  phone = '+61478638278'

  stringsesh = asyncio.run(first_log_in(phone, api_id, api_hash))
  print("finished up")
  print(stringsesh)

main_loop()
