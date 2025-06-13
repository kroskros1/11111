import os
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from bot.handlers import setup_handlers
from bot.config import TOKEN, PORT

def main():
    # Видаліть use_context=True
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    setup_handlers(dp)

    if 'RENDER' in os.environ:
        updater.start_webhook(
            listen="0.0.0.0",
            port=PORT,
            url_path=TOKEN,
            webhook_url=f"https://your-render-app.onrender.com/{TOKEN}"
        )
    else:
        updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
