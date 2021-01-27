from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from base.constants import *
import random
import telegram, time
import sqlite3


def buttons(update, context):
    chat_id = update.message.chat_id
    top_buttons_list = [
        InlineKeyboardButton(text=t1, callback_data='cro')
    ]
    mid_buttons_list = [
        InlineKeyboardButton(text=t2, callback_data='numb')
    ]
    bot_buttons_list = [
        InlineKeyboardButton(text=t3, callback_data='fate')
    ]
    print(chat_id, 'clicked')

    context.bot.send_message(
        text='Что выберете?',
        chat_id=chat_id,
        reply_markup=InlineKeyboardMarkup([top_buttons_list, mid_buttons_list, bot_buttons_list
                                           ])
    )


def numb(update, context):
    try:
        chat_id = update.callback_query.from_user.id
    except:
        chat_id = update.message.from_user.id
    conn = sqlite3.connect(PATH_TO_DB)
    cursor = conn.cursor()
    cursor.execute('''
                                       insert into RandomNumbers values('{}', '{}')
                                       '''.format(id, random.randint(1000, 10000)))

    print(chat_id, 123)
    conn = sqlite3.connect(PATH_TO_DB)
    cur = conn.cursor()
    cur.execute('''update IdentifiedUsers 
                   set status=2 
                   where id='{}'
                '''.format(chat_id))
    conn.commit()
    context.bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.TYPING)
    context.bot.send_message(chat_id=chat_id,
                             text=number)
    time.sleep(3)

    context.bot.send_message(chat_id=chat_id,
                             text='И так... Загадываю число')
    context.bot.send_chat_action(chat_id=chat_id,
                                 action=telegram.ChatAction.TYPING)
    time.sleep(7)
    context.bot.send_message(chat_id=chat_id,
                             text='Ну всё... Поехали')
