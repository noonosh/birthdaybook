from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext
from util.language import lang
from lib.text import t, b


class Home():

    def display(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        language = lang(chat_id)
        markup = [
            [b('addBirthday', language)],
            [b('myFriends', language), b('myInfo', language)],
            [b('inviteFriend', language)]
        ]

        update.effective_message.reply_text("Home page",
                                            reply_markup=ReplyKeyboardMarkup(
                                                markup, resize_keyboard=True
                                            ),
                                            parse_mode='HTML')
