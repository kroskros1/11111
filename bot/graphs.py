import matplotlib.pyplot as plt
import numpy as np
import io
from telegram import Update
from telegram.ext import CallbackContext

def generate_graph(section: str):
    plt.figure(figsize=(8, 4))
    x = np.linspace(0, 10, 100)
    if section == 'cutting':
        y = np.sin(x) * np.random.uniform(0.8, 1.2, 100)
        plt.title('Графік розкрою')
    elif section == 'arming':
        y = np.cos(x) * np.random.uniform(0.7, 1.3, 100)
        plt.title('Графік армування')
    # ... (аналогічно для інших дільниць)
    
    plt.plot(x, y)
    plt.grid(True)
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()
    return buf

def show_graph(update: Update, context: CallbackContext, section: str):
    graph = generate_graph(section)
    update.callback_query.message.reply_photo(photo=graph, caption=f"Графік для дільниці: {section}")