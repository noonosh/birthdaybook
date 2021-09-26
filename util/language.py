from util.database import cursor


def lang(chat_id):
    cursor.execute(
        "SELECT language_code FROM users WHERE id='{}'".format(chat_id))
    user = cursor.fetchone()
    return user[0]
