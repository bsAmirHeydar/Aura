from bot.telegram_bot import create_bot

TOKEN = "7216545327:AAHDPe-eMtqmSdX1uvShZok5McONbHP0dEA"

def main():
    app = create_bot(TOKEN)
    app.run_polling()

if __name__ == "__main__":
    main()