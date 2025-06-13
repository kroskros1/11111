from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, CallbackQueryHandler, CommandHandler
from bot.keyboards import main_menu_markup, sections_markup

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Вітаю в системі автоматизації!", reply_markup=main_menu_markup())

def graphs_menu(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="Оберіть дільницю:", reply_markup=sections_markup())

def setup_handlers(dp):
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CallbackQueryHandler(graphs_menu, pattern='graphs_menu'))
    # ... (решта обробників)