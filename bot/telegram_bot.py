# from telegram.ext import Application, CommandHandler, MessageHandler, filters
# from . import handlers

# def create_bot(token: str):
#     app = Application.builder().token(token).build()

#     # هندلرها
#     app.add_handler(CommandHandler("start", handlers.start))
#     app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handlers.echo))

#     return app

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

from ai.rag import RAG
from ai.deepseek import ask_deepseek

# بارگذاری همه فایل‌های Word از پوشه data
rag = RAG("data")

# نقش و لحن ربات
SYSTEM_ROLE = "You are a friendly but respectful assistant to customers at a car dealership. Answer only based on the information provided."
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello 👋 I'm ready to help you with the terms of buying a car.")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    # جستجو در دیتا
    context_text = "\n".join(rag.search(user_text))

    # پرسش از مدل
    response = ask_deepseek(SYSTEM_ROLE, context_text, user_text)

    await update.message.reply_text(response)

def create_bot(token: str):
    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    return app
