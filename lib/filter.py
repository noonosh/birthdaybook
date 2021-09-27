
from telegram.ext import MessageFilter
from lib.text import j


class FilterButton(MessageFilter):
    def __init__(self, key: str):
        self.key = key

    def filter(self, message):
        langs = j["button"][self.key]
        buttons = []
        for i in langs:
            buttons.append(langs[i])
        return message.text in buttons
