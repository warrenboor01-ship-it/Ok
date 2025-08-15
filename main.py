import os
import asyncio
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")  # Set your bot token as an environment variable
CHAT_ID = os.getenv("CHAT_ID")      # The group/chat ID where the bot will send messages

MESSAGE_TEXT = "@EagleMEVBot For free money while you sleep"

async def send_messages():
    bot = Bot(token=BOT_TOKEN)
    while True:
        try:
            await bot.send_message(chat_id=CHAT_ID, text=MESSAGE_TEXT)
            print("Message sent.")
        except Exception as e:
            print(f"Error: {e}")
        await asyncio.sleep(20)  # Wait 20 seconds before sending again

if __name__ == "__main__":
    asyncio.run(send_messages())
