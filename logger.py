from telegram import Update
from datetime import datetime as dt

def log(update: Update, title):
    time = dt.now().strftime('%d.%m.%Y-%H:%M')
    with open('calc_bot.txt', 'a',encoding="utf8") as file: 
        file.write(f'{time}: {update.effective_user.first_name}, {update.effective_user.id} - {title}\n')

