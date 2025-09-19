from telegram.ext import Application, CommandHandler, MessageHandler, filters
from . import handlers

def create_bot(token: str):
    app = Application.builder().token(token).build()

    # هندلرها
    app.add_handler(CommandHandler("start", handlers.start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handlers.echo))

    return app
