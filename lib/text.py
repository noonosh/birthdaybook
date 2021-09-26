import json

j = json.load(open("lib/text.json", "r", encoding="utf-8"))


def t(key: str, lang: str):
    """b Function that gets the text for the bot from text.json
    Args:
        key (str): [key for the json to find the right piece of text]
        lang (str): [language of the given text]
    Returns:
        [str]: [Text from texts.json]
    """
    return j["text"][key][lang]


def b(key: str, lang: str):
    """b Function that gets the text of a button in the bot from text.json
    Args:
        key (str): [key for the json to find the right piece of text]
        lang (str): [language of the given text]
    Returns:
        [str]: [Text from texts.json]
    """
    return j["button"][key][lang]
