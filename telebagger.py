from telethon import TelegramClient, events, sync, utils
from telethon.sessions import StringSession
import requests


def SendMessageToAlwaysWin(message):
    message= "<@&834911692303237172>\n" + message
    mUrl = "https://ptb.discord.com/api/webhooks/838079506660851762/7-lpGNlqWGGlO08XZJ3RwAvSXpWGDf5J6Z4ro5bsdtogYGGXovVfmYGmCb3Jvr1RvtWG"
    data = {"content": message}
    response = requests.post(mUrl, json=data)

def StartTelegramForwarding():
    api_id = 5747368
    api_hash = '19f6d3c9d8d4e6540bce79c3b9223fbe'
    stringsesh = '1BVtsOIIBuziBvZO_VwaerS4NJoP1vAyxIiLLYPdQNn2lXhRFMH2GY_ayqJEM-ax5I-GD4-Kk_lCPjXBTxpmyaDO-hKYeYSyjNYYZ3riEVwFnsy4PGwrXxRwdiKZrICrcEKih0yoTO7lVDO8APaiDpx3E2pFDXyYRhd66Rnj0UyDEcnHPRstadaNTN34BBtLtl7T3LwxQn58ka8sZVRdKAscBjLwiwj8IF4Lwu0oHAH20Ozd5mh8ior82nBz1MRha_C-o6ehdPwhSHFBCCzBqw_zcJ7RjNeeWS4BZ2Jn6XlHatuTXctaMieFymtJkCtEK2gJj9eaf9v5EZGoc1vp9liZ_ra7A7pA='
    client = TelegramClient(StringSession(stringsesh), api_id, api_hash)
    dialogue = client.get_dialogs()
    
    @client.on(events.NewMessage()) 
    async def my_event_handler(event):
        print(event.raw_text)

        sender = await event.get_sender()
        chat = await event.get_chat()
        sender_id = str(sender.id)
        channel_name = utils.get_display_name(sender)
        msg = "Channel name: " + channel_name + " | ID: " + sender_id
        print(msg)
        if sender_id == "1375168387":
            SendMessageToAlwaysWin(event.raw_text)
        elif chat.id == 1899129008:
            print("Robot Section +++")
            if str(event.raw_text) == '/stop':
              print('Exiting....')
              await client.disconnect()

    print("Starting telegram scraper")
    client.start()
    client.run_until_disconnected()

StartTelegramForwarding()
