# from telegram import Update
# from telegram.ext import ContextTypes
# from ai.deepseek import call_deepseek

# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("Hi, I'm Heydar Khodro")

# async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user_text = update.message.text
    
#     response = call_deepseek(user_text)  # می‌ره سراغ مدل DeepSeek
    
#     await update.message.reply_text(response)

# bot/handlers.py
from telegram import Update
from telegram.ext import ContextTypes
from ai.deepseek import ask_deepseek

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام 👋 من آماده‌ام، هر چی خواستی بپرس.")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    user_text = update.message.text

    response = ask_deepseek(user_id, user_text)

    await update.message.reply_text(response)
