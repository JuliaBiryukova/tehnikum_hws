import time, telegram
from constants import *
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def typing(update, context):
    context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    time.sleep(2)


def cro(update, context):
    typing(update, context)
    context.bot.send_message(chat_id=update.message.chat_id,
                             text=crocodile)
    cro_butt(update, context)


def cro_butt(update, context):
    chat_id = update.message.chat_id
    top_buttons_list = [InlineKeyboardButton(text='1', callback_data='qsn1'),
                        InlineKeyboardButton(text='2', callback_data='qsn2')]
    mid_buttons_list = [InlineKeyboardButton(text='3', callback_data='qsn3'),
                        InlineKeyboardButton(text='4', callback_data='qsn4')]
    bot_buttons_list = [InlineKeyboardButton(text='5', callback_data='qsn5'),
                        InlineKeyboardButton(text='6', callback_data='qsn6'),
                        InlineKeyboardButton(text='7', callback_data='qsn7')]
    print(chat_id, 'clicked')

    context.bot.send_message(
        text='Что выберете?',
        chat_id=chat_id,
        reply_markup=InlineKeyboardMarkup([top_buttons_list, mid_buttons_list, bot_buttons_list
                                           ])
    )


def qsn1(update, context):
    user_id = update.callback_query.from_user.id
    top_buttons_list = [InlineKeyboardButton(text='шмель', callback_data='rght'),
                        InlineKeyboardButton(text='птица', callback_data='wrn')]
    mid_buttons_list = [InlineKeyboardButton(text='гусеница', callback_data='wrn'),
                        InlineKeyboardButton(text='что-то другое', callback_data= 'wrn')]

    context.bot.send_message(chat_id=user_id,
                             text=qtn1,
                             reply_markup=InlineKeyboardMarkup([top_buttons_list,mid_buttons_list]))


def qsn2(update, context):
    user_id = update.callback_query.from_user.id
    top_buttons_list = [InlineKeyboardButton(text='не знаю даже', callback_data='wrn'),
                        InlineKeyboardButton(text='учитель', callback_data='wrn')]
    mid_buttons_list = [InlineKeyboardButton(text='петух', callback_data='rght'),
                        InlineKeyboardButton(text='гусь', callback_data='wrn')]
    context.bot.send_message(chat_id=user_id,
                             text=qtn2,
                             reply_markup=InlineKeyboardMarkup([top_buttons_list,mid_buttons_list]))

def qsn3(update, context):
    user_id = update.callback_query.from_user.id
    top_buttons_list = [InlineKeyboardButton(text='Гитлер)', callback_data='wrn'),
                        InlineKeyboardButton(text='моржик', callback_data='wrn')]
    mid_buttons_list = [InlineKeyboardButton(text='кот', callback_data='rght'),
                        InlineKeyboardButton(text='пёсель', callback_data='wrn')]
    context.bot.send_message(chat_id=user_id,
                             text=qtn3,
                             reply_markup=InlineKeyboardMarkup([top_buttons_list,mid_buttons_list]))


def qsn4(update, context):
    user_id = update.callback_query.from_user.id
    top_buttons_list = [InlineKeyboardButton(text='Петь', callback_data='wrn'),
                        InlineKeyboardButton(text='Повеситься', callback_data='rght')]
    mid_buttons_list = [InlineKeyboardButton(text='Пить', callback_data='wrn'),
                        InlineKeyboardButton(text='Гулять', callback_data='wrn'),
                        InlineKeyboardButton(text='Всё можно)', callback_data='wrn')]
    context.bot.send_message(chat_id=user_id,
                             text=qtn5,
                             reply_markup=InlineKeyboardMarkup([top_buttons_list,mid_buttons_list]))

def qsn5(update, context):
    user_id = update.callback_query.from_user.id
    top_buttons_list = [InlineKeyboardButton(text='Что-то другое', callback_data='wrn'),
                        InlineKeyboardButton(text='Кондуктор', callback_data='rght')]
    mid_buttons_list = [InlineKeyboardButton(text='Бич', callback_data='wrn'),
                        InlineKeyboardButton(text='Точно не та, о которой подумал)', callback_data='wrn')]
    context.bot.send_message(chat_id=user_id,
                             text=qtn6,
                             reply_markup=InlineKeyboardMarkup([top_buttons_list,mid_buttons_list]))


def qsn6(update, context):
    user_id = update.callback_query.from_user.id
    top_buttons_list = [InlineKeyboardButton(text='Точно не Брежнев', callback_data='wrn'),
                        InlineKeyboardButton(text='Креветочка', callback_data='wrn')]
    mid_buttons_list = [InlineKeyboardButton(text='Котик', callback_data='wrn'),
                        InlineKeyboardButton(text='Таракулька', callback_data='rght')]
    context.bot.send_message(chat_id=user_id,
                             text=qtn7,
                             reply_markup=InlineKeyboardMarkup([top_buttons_list,mid_buttons_list]))


def qsn7(update, context):
    user_id = update.callback_query.from_user.id
    top_buttons_list = [InlineKeyboardButton(text='Свечку', callback_data='wrn'),
                        InlineKeyboardButton(text='Г.Лампу', callback_data='wrn')]
    mid_buttons_list = [InlineKeyboardButton(text='Спичку', callback_data='rght'),
                        InlineKeyboardButton(text='К.Лампу', callback_data='wrn'),
                        InlineKeyboardButton(text='Не знаю', callback_data='dknw')]
    context.bot.send_message(chat_id=user_id,
                             text=qtn8,
                             reply_markup=InlineKeyboardMarkup([top_buttons_list,mid_buttons_list]))


def rght(update, context):
    chat_id = update.callback_query.from_user.id
    context.bot.send_message(chat_id=chat_id,
                             text=ans1)
    context.bot.send_message(chat_id=chat_id,
                             text='Следующий вопросик)')


def wrng(update, context):
    context.bot.send_message(chat_id=update.callback_query.from_user.id,
                             text=ans)

def dknw(update, context):
    context.bot.send_message(chat_id=update.callback_query.from_user.id,
                             text=ans2)
