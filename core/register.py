from telegram import (Update,
                      InlineKeyboardButton,
                      InlineKeyboardMarkup, chat)
from telegram.ext import CallbackContext
from core.home import Home
from util.database import cursor, connection
from util.language import lang
from lib.text import t, b
import logging
import datetime


class Register():

    def begin(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        logging.info("%s - New registration started", chat_id)
        buttons = [
            [InlineKeyboardButton(b('language', 'en'), callback_data='en')],
            [InlineKeyboardButton(b('language', 'ru'), callback_data='ru')],
            [InlineKeyboardButton(b('language', 'uz'), callback_data='uz')]
        ]

        cursor.execute(
            "INSERT INTO users (id, last_active) VALUES ('{}', '{}')".format(chat_id, datetime.datetime.now()))
        connection.commit()
        update.effective_message.reply_text(
            f"{t('chooseLanguage', 'en')}\n{t('chooseLanguage', 'ru')}\n{t('chooseLanguage', 'uz')}",
            reply_markup=InlineKeyboardMarkup(
                buttons),
            parse_mode="HTML"
        )
        logging.info("%s - Requested for language preferences", chat_id)
        return "LANGUAGE"

    def save_language(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        query = update.callback_query
        data = query.data
        logging.info("%s - Language preferences saved", chat_id)
        query.answer()
        query.delete_message()

        cursor.execute("UPDATE users SET language_code = '{}' WHERE id = '{}'"
                       .format(data, chat_id))
        connection.commit()
        update.effective_message.reply_text("Great!")
        return self.request_name(update, context)

    def request_name(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        language = lang(chat_id)

        update.effective_message.reply_text(t('nameRequest', language),
                                            parse_mode="HTML")
        logging.info("%s - Requested for name", chat_id)
        return "NAME REQUESTED"

    def save_name(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        name = update.message.text

        cursor.execute(
            "UPDATE users SET first_name = '{}' WHERE id = '{}'".format(name, chat_id))
        connection.commit()

        return self.quick_registration_complete(update, context)

    def quick_registration_complete(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        language = lang(chat_id)
        update.effective_message.reply_text(t('quickRegister', language),
                                            parse_mode="HTML")
        return Home().display(update, context)
