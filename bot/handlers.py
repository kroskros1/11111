from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
    MessageHandler,
    filters
)
from bot.keyboards import (
    main_menu_markup,
    sections_markup,
    settings_markup,
    language_markup,
    frequency_markup,
    admin_panel_markup
)
from bot.graphs import show_graph
from bot.admin import view_logs, add_user
from bot.logs import generate_logs
from bot.settings import change_language, change_frequency
from bot.database import set_threshold

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Вітаємо в системі автоматизації виробництва вікон!",
        reply_markup=main_menu_markup()
    )

async def main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        text="Головне меню:",
        reply_markup=main_menu_markup()
    )

async def graphs_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        text="Оберіть дільницю:",
        reply_markup=sections_markup()
    )

async def thresholds_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        text="Введіть поріг для дільниці у форматі: 'дільниця значення' (наприклад: 'cutting 60')"
    )

async def handle_threshold(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        text = update.message.text.split()
        section = text[0]
        value = float(text[1])
        set_threshold(section, value)
        await update.message.reply_text(
            f"Поріг для {section} встановлено на {value}",
            reply_markup=main_menu_markup()
        )
    except Exception as e:
        await update.message.reply_text("Невірний формат. Спробуйте ще раз.")

async def download_logs(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    logs = generate_logs()
    await context.bot.send_document(
        chat_id=query.message.chat_id,
        document=logs,
        filename='logs.txt'
    )

async def settings_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        text="Налаштування:",
        reply_markup=settings_markup()
    )

async def admin_panel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        text="👑 Адмін панель",
        reply_markup=admin_panel_markup()
    )

def setup_handlers(application: Application) -> None:
    # Команди
    application.add_handler(CommandHandler("start", start))
    
    # Головне меню
    application.add_handler(CallbackQueryHandler(main_menu, pattern="main_menu"))
    
    # Графіки
    application.add_handler(CallbackQueryHandler(graphs_menu, pattern="graphs_menu"))
    application.add_handler(CallbackQueryHandler(lambda u, c: show_graph(u, c, 'cutting'), pattern="graph_cutting"))
    application.add_handler(CallbackQueryHandler(lambda u, c: show_graph(u, c, 'arming'), pattern="graph_arming"))
    application.add_handler(CallbackQueryHandler(lambda u, c: show_graph(u, c, 'welding'), pattern="graph_welding"))
    application.add_handler(CallbackQueryHandler(lambda u, c: show_graph(u, c, 'cleaning'), pattern="graph_cleaning"))
    application.add_handler(CallbackQueryHandler(lambda u, c: show_graph(u, c, 'glazing'), pattern="graph_glazing"))
    application.add_handler(CallbackQueryHandler(lambda u, c: show_graph(u, c, 'control'), pattern="graph_control"))
    
    # Пороги
    application.add_handler(CallbackQueryHandler(thresholds_menu, pattern="thresholds_menu"))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_threshold))
    
    # Логи
    application.add_handler(CallbackQueryHandler(download_logs, pattern="download_logs"))
    
    # Налаштування
    application.add_handler(CallbackQueryHandler(settings_menu, pattern="settings_menu"))
    application.add_handler(CallbackQueryHandler(change_language, pattern="change_language"))
    application.add_handler(CallbackQueryHandler(change_frequency, pattern="change_frequency"))
    
    # Адмін-панель
    application.add_handler(CallbackQueryHandler(admin_panel, pattern="admin_panel"))
    application.add_handler(CallbackQueryHandler(view_logs, pattern="view_logs"))
    application.add_handler(CallbackQueryHandler(add_user, pattern="add_user"))
