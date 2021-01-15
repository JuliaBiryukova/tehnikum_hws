from telegram import KeyboardButton, ReplyKeyboardMarkup
from constants import *
import random, telegram
import time

def numb(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text=number)
    a = 0
    context.bot.send_message(chat_id=update.message.chat_id,
                             text='Введите два числа:')
    z = int(input())
    x = int(input())
    n = random.randint(z, x)
    context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    time.sleep(3)
    context.bot.send_message(chat_id=update.message.chat_id,
                             text='Хорошо!')
    while True:
        context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
        time.sleep(2)
        context.bot.send_message(chat_id=update.message.chat_id,
                                 text='Ваш ответ:' + '{}')
        if int(update.message.text) > n:
            context.bot.send_message(chat_id=update.message.chat_id,
                                     text='Моё число меньше твоего')
            context.bot.send_message(chat_id=update.message.chat_id,
                                     text='Думай Кузя, Думай!')
        elif int(update.message.text) < n:
            context.bot.send_message(chat_id=update.message.chat_id,
                                     text='Моё число больше твоего')
            context.bot.send_sticker(chat_id=update.callback_query.from_user.id,
                                     sticker='CAACAgIAAxkBAAKxuGABvB-qYvGGoHP-J7pC-dM5ihm9AAJDgQACns4LAAEIT4bAC7UqGR4E')
        elif (int(update.message.text) == n + 1) or (int(update.message.text) == n - 1):
            context.bot.send_message(chat_id=update.message.chat_id,
                                     text='Горячо!')
            context.bot.send_sticker(chat_id=update.callback_query.from_user.id,
                                     sticker='CAACAgIAAxkBAAKxzWABx0sqUAEJe-gP2A6PRmt2Jkb-AAJKAANH-wkMS4BHVUtTO2UeBA')
        elif (int(update.message.text) == n + 3) or (int(update.message.text) == n - 3):
            context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
            time.sleep(2)
            context.bot.send_message(chat_id=update.message.chat_id,
                                     text='Тепло!')
        elif int(update.message.text) == n:
            break
        else:
            context.bot.send_message(chat_id=update.message.chat_id,
                                     text='Холодно')
            context.bot.send_sticker(chat_id=update.callback_query.from_user.id,
                                     sticker='CAACAgIAAxkBAAKx0GAByJ1KoDYWUSzxCQKeA8isshx6AAJIAANH-wkMbIxNWYsX_SgeBA')

    context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    time.sleep(2)
    context.bot.send_message(chat_id=update.message.chat_id,
                             text='Ну что ж..., Не плохо, не плохо')
    context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    time.sleep(2)
    context.bot.send_message(chat_id=update.message.chat_id,
                             text='Хочешь продолжить?')

    if update.message.text == 'да':
        numb(update,context)
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
