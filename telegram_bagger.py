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

