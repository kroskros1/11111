import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
PORT = int(os.getenv('PORT', 8443))
ADMIN_IDS = list(map(int, os.getenv('ADMIN_IDS', '').split(',')))