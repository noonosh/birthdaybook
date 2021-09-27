from telegram.ext import (Updater,
                          CallbackContext,
                          ConversationHandler,
                          CommandHandler,
                          CallbackQueryHandler,
                          MessageHandler,
                          Filters)
from telegram import Update
from core.home import Home
from core.command import Command
from core.register import Register
from lib.filter import FilterButton
import os
import dotenv
import logging

# Load environment variables
dotenv.load_dotenv()

# Debugging configuration
DEBUG = os.environ.get('DEBUG', False) == 'True'

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG if DEBUG else logging.INFO
)
logger = logging.getLogger(__name__)

home = Home()
command = Command()
register = Register()


def main():
    TOKEN = os.getenv('BOT_TOKEN')
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    main_conversation = ConversationHandler(
        entry_points=[
            CommandHandler('start', command.start)
        ],
        states={
            "LANGUAGE": [
                CallbackQueryHandler(
                    register.save_language, pattern='en|ru|uz')
            ],
            "NAME REQUESTED": [
                MessageHandler(Filters.text, register.save_name)
            ],
            "HOME": [
                MessageHandler(FilterButton("addBirthday"), home.add_birthday)
            ]
        },
        fallbacks=[]
    )

    dispatcher.add_handler(main_conversation)

    updater.start_polling()
    updater.idle()
