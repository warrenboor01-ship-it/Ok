import os
import time
from telegram import Bot

# Load bot token and group chat ID from environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")  # Example: -1001234567890

bot = Bot(token=BOT_TOKEN)

def main():
    while True:
        try:
            bot.send_message(chat_id=CHAT_ID, text="@EagleMEVBot For free money while you sleep")
            print("Message sent!")
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(20)  # Wait 20 seconds

if __name__ == "__main__":
    main()