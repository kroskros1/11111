from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from bot.database import get_settings

# Головне меню
def main_menu_markup():
    keyboard = [
        [InlineKeyboardButton("📈 Графіки", callback_data='graphs_menu')],
        [InlineKeyboardButton("⚙️ Пороги", callback_data='thresholds_menu')],
        [InlineKeyboardButton("📁 Вивантаження логів", callback_data='download_logs')],
        [InlineKeyboardButton("🛠️ Налаштування", callback_data='settings_menu')],
        [InlineKeyboardButton("👑 Адмін панель", callback_data='admin_panel')]
    ]
    return InlineKeyboardMarkup(keyboard)

# Меню дільниць для графіків
def sections_markup():
    keyboard = [
        [InlineKeyboardButton("Розкрій", callback_data='graph_cutting')],
        [InlineKeyboardButton("Армування", callback_data='graph_arming')],
        [InlineKeyboardButton("Зварювання", callback_data='graph_welding')],
        [InlineKeyboardButton("Зачистка", callback_data='graph_cleaning')],
        [InlineKeyboardButton("Скління", callback_data='graph_glazing')],
        [InlineKeyboardButton("Контроль", callback_data='graph_control')],
        [InlineKeyboardButton("⬅️ Назад", callback_data='main_menu')]
    ]
    return InlineKeyboardMarkup(keyboard)

# Меню налаштувань
def settings_markup():
    settings = get_settings()
    keyboard = [
        [InlineKeyboardButton(f"Мова: {settings['language']}", callback_data='change_language')],
        [InlineKeyboardButton(f"Частота оновлення: {settings['update_frequency']} хв", callback_data='change_frequency')],
        [InlineKeyboardButton("⬅️ Назад", callback_data='main_menu')]
    ]
    return InlineKeyboardMarkup(keyboard)

# Вибір мови
def language_markup():
    keyboard = [
        [InlineKeyboardButton("Українська (UA)", callback_data='set_language_UA')],
        [InlineKeyboardButton("English (EN)", callback_data='set_language_EN')],
        [InlineKeyboardButton("⬅️ Назад", callback_data='settings_menu')]
    ]
    return InlineKeyboardMarkup(keyboard)

# Вибір частоти оновлення
def frequency_markup():
    keyboard = [
        [InlineKeyboardButton("15 хвилин", callback_data='set_frequency_15')],
        [InlineKeyboardButton("30 хвилин", callback_data='set_frequency_30')],
        [InlineKeyboardButton("1 година", callback_data='set_frequency_60')],
        [InlineKeyboardButton("⬅️ Назад", callback_data='settings_menu')]
    ]
    return InlineKeyboardMarkup(keyboard)

# Адмін-панель
def admin_panel_markup():
    keyboard = [
        [InlineKeyboardButton("Переглянути логи", callback_data='view_logs')],
        [InlineKeyboardButton("Додати користувача", callback_data='add_user')],
        [InlineKeyboardButton("⬅️ Назад", callback_data='main_menu')]
    ]
    return InlineKeyboardMarkup(keyboard)