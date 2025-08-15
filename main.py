import os
import time
from telegram import Bot

# Load environment variables set in Railway
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = int(os.environ.get("CHAT_ID"))

bot = Bot(token=BOT_TOKEN)

print("Bot started!")

while True:
    try:
        bot.send_message(chat_id=CHAT_ID, text="@EagleMEVBot For free money while you sleep")
        print("Message sent!")
    except Exception as e:
        print(f"Error sending message: {e}")
    time.sleep(20)  # Wait 20 seconds before sending the next message