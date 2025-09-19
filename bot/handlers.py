from telegram import Update
from telegram.ext import ContextTypes
from ai.deepseek import call_deepseek

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("View")

# async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user_text = update.message.text
#     response = f"تو گفتی: {user_text}"
#     await update.message.reply_text(response)
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    
    response = call_deepseek(user_text)  # می‌ره سراغ مدل DeepSeek
    
    await update.message.reply_text(response)

# from telegram import Update
# from telegram.ext import ContextTypes
# from ai.deepseek_client import call_deepseek

# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("AuraFlow + DeepSeek آماده‌ست 🚀")

# async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user_text = update.message.text
    
#     # ارسال پیام به مدل DeepSeek
#     response = call_deepseek(user_text)
    
#     await update.message.reply_text(response)
