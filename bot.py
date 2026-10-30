import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👻 Welcome to Harrington Horror Studio!\n\n"
        "Apni horror story bhejo. Video generator jald ready hoga!"
    )

async def receive_story(update: Update, context: ContextTypes.DEFAULT_TYPE):
    story = update.message.text

    await update.message.reply_text(
        "🎬 Your horror story received!\n\n"
        "Story processing system abhi development mein hai.\n"
        "Jald hi video generation shuru hogi!"
    )

def main():
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN is missing!")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, receive_story))

    print("Harrington Horror Studio is running!")
    app.run_polling()

if __name__ == "__main__":
    main()
