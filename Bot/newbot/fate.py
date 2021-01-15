from telegram import KeyboardButton, ReplyKeyboardMarkup
import telegram, time, random
from fate_text import *
def fate(update, context):
    while True:
        context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
        time.sleep(5)
        context.bot.send_message(chat_id=update.message.chat_id, text='Готов узнать своё послание?')
        ft = random.randint(a, z)
        if update.message.text == 'да':
            context.bot.send_message(chat_id=update.message.chat_id, text=ft)

        context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
        time.sleep(5)
        context.bot.send_message(chat_id=update.message.chat_id, text='Продолжим?')
        if update.message.text == 'да':
            context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
            time.sleep(3)
            ft = random.randint(a, z)
            context.bot.send_message(chat_id=update.message.chat_id, text=ft)
        if update.message.text == 'нет':
            chat_id = update.message.chat_id
            buttons_list = [
                KeyboardButton(text='Кроко', callback_data='clicked'),
                KeyboardButton(text='Отгадай число', callback_data='clicked'),
                KeyboardButton(text='Послание из будущего', callback_data='clicked')
            ]
            print(chat_id, 'clicked')

            context.bot.send_message(
                text='Choose button:',
                chat_id=chat_id,
                reply_markup=ReplyKeyboardMarkup([buttons_list
                                                  ])
            )
