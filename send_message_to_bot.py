#!/usr/bin/python3.6
#
# usage: send_message_to_bot.py <message>
#
# simply send a message to your telegram bot

import sys
import asyncio
import asyncio.subprocess
from telethon import TelegramClient

api_id    =  0 # your telegram api id
api_hash  =  0 # your telegram api hash
bot_token =  0 # your bot_token
admin_id  =  0 # your chat id

async def send_message(bot, msg):
    await bot.send_message(admin_id, msg, parse_mode='md')

if __name__ == "__main__":
    bot = TelegramClient('tg_msg_send_bot', api_id, api_hash).start(bot_token=str(bot_token))
    message = sys.argv[1] if len(sys.argv) >= 2 else ""
    loop = asyncio.get_event_loop()
    loop.run_until_complete(send_message(bot, message))
