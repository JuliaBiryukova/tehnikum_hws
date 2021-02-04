import random, telegram, time
from fate_text import *
from constants import *
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def fate(update, context):

    chat_id = update.message.chat_id
    context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    time.sleep(2)
    ft_butt = [InlineKeyboardButton(text='Да!', callback_data='poslaniye'),
               InlineKeyboardButton(text='Конечно', callback_data='poslaniye')]
    print(chat_id, 'clicked')

    context.bot.send_message(
        text=fate1,
        chat_id=chat_id,
        reply_markup=InlineKeyboardMarkup([ft_butt
                                            ])
    )


def poslaniye(update, context):
    chat_id = update.callback_query.from_user.id
    context.bot.send_message(chat_id=chat_id, text=poslaniye1)
    context.bot.send_message(chat_id=chat_id, text=poslaniye2)
    b = len(a)
    c = random.randint(1, b)
    context.bot.send_message(chat_id=chat_id, text=a[c])
    context.bot.send_message(chat_id=chat_id, text=numb8)
