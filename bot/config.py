import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
PORT = int(os.getenv('PORT', 8443))

# Виправлений код для ADMIN_IDS
admin_ids_str = os.getenv('ADMIN_IDS', '')
ADMIN_IDS = [int(id_str) for id_str in admin_ids_str.split(',') if id_str.strip()] if admin_ids_str else []
