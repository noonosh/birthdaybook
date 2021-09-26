from telegram import Update
from telegram.ext import CallbackContext
from util.private import is_private_chat
from util.database import cursor
from core.register import Register


class Command():

    def start(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id

        cursor.execute("SELECT * FROM users WHERE id = '{}'".format(chat_id))
        user = cursor.fetchone()

        if is_private_chat(chat_id) and user is None:
            return Register().begin(update, context)
        else:
            return
