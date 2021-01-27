import sqlite3, requests
from numberss import *
from fate import *
from crocodile import *


def typing(update, context):
    context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    time.sleep(3)


def contact(update,context):
    context.bot.send_message(chat_id=update.message.chat_id, text='контакт получен')


def start(update, context):
    name = update.message.from_user.first_name
    id = update.message.chat_id
    context.bot.send_message(chat_id=update.message.chat_id,
                             text=start_msg + name)


    conn = sqlite3.connect(PATH_TO_DB)
    cursor = conn.cursor()

    user_exists = cursor.execute('''
       select id
       from NewUsers
       where id= '{}'
       '''.format(id)).fetchall()
    print(user_exists)
    if len(user_exists) == 0:
        cursor.execute('''
           insert into NewUsers values('{}', '{}','0',  '{}')
           '''.format(id, name, random.randint(1000, 10000)))
        cursor.execute('''
                           insert into IdentifiedUsers values('{}', '0')
                           '''.format(id))

        conn.commit()
    context.bot.send_message(chat_id=update.message.chat_id,
                             text=phone)


def text(update, context):
    conn = sqlite3.connect(PATH_TO_DB)
    cursor = conn.cursor()
    status = cursor.execute('''
            select status
            from IdentifiedUsers
            where id= '{}'
            '''.format(update.message.chat_id)).fetchall()[0][0]
    print(status)

    if update.message.text.isalnum and len(update.message.text) == 4 and status == 0:
        conn = sqlite3.connect(PATH_TO_DB)
        cursor = conn.cursor()
        id = update.message.chat_id

        user_code = cursor.execute('''
            select code
            from NewUsers
            where id= '{}'
            '''.format(id)).fetchall()[0][0]

        if int(update.message.text) == int(user_code):
            typing(update, context)
            context.bot.send_message(chat_id=id, text='Правильно!')
            choose_game(context, update)
        else:
            typing(update, context)
            context.bot.send_message(chat_id=id, text='Проверьте ваш код...')
    elif update.message.text.isalnum and len(update.message.text) == 12 and status == 0:
        conn = sqlite3.connect(PATH_TO_DB)
        cursor = conn.cursor()
        id = update.message.chat_id
        context.bot.send_message(chat_id=id, text='Спасибки, проверьте ваши смс')

        user_code = cursor.execute('''
                        select code
                        from NewUsers
                        where id= '{}'
                        '''.format(id)).fetchall()[0][0]

        requests.post(URL, data={'token': SMS_TOKEN,
                                 'sms_phone': int(update.message.text),
                                 'sms_text': str(user_code)})
    elif update.message.text.isalnum and status == 2:
        numberio(update, context)


def numberio(update, context):
    print(1)
    nmb = int(update.message.text)
    context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    time.sleep(2)
    context.bot.send_message(chat_id=update.message.chat_id,
                             text='Ваш ответ:' + str(nmb))

    conn = sqlite3.connect(PATH_TO_DB)
    cursor = conn.cursor()
    n = int(cursor.execute('''
        select rand_number
        from RandomNumbers
    ''').fetchall()[0][0])
    if nmb > n:
        context.bot.send_message(chat_id=update.message.chat_id,
                                 text=numb1)
        context.bot.send_message(chat_id=update.message.chat_id,
                                 text=numb2)
    elif nmb < n:
        context.bot.send_message(chat_id=update.message.chat_id,
                                 text=numb3)
    elif (nmb == n + 1) or (nmb == n - 1):
        context.bot.send_message(chat_id=update.message.chat_id,
                                 text=numb4)
    elif (nmb == n + 3) or (nmb == n - 3):
        context.bot.send_message(chat_id=update.message.chat_id,
                                 text=numb5)
    elif nmb == n:
        context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
        time.sleep(1)
        context.bot.send_message(chat_id=update.message.chat_id,
                                 text=numb7)
        context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
        time.sleep(1)
        buttons(update, context)
    else:
        context.bot.send_message(chat_id=update.message.chat_id,
                                 text=numb6)


def choose_game(context, update):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text='Введите код')
    typing(update, context)
    context.bot.send_message(chat_id=update.message.chat_id,
                             text=tnk)
    typing(update, context)
    context.bot.send_message(chat_id=update.message.chat_id,
                             text=first)
    typing(update, context)
    users_id = update.message.chat_id
    context.bot.send_message(chat_id=update.message.chat_id,
                             text=intro)
    top_buttons_list = [
        InlineKeyboardButton(text=t1, callback_data='cro')
    ]
    mid_buttons_list = [
        InlineKeyboardButton(text=t2, callback_data='numb')
    ]
    bot_buttons_list = [
        InlineKeyboardButton(text=t3, callback_data='fate')
    ]
    print(users_id, 'clicked')
    context.bot.send_message(
        text='Что выберете?',
        chat_id=users_id,
        reply_markup=InlineKeyboardMarkup([top_buttons_list, mid_buttons_list, bot_buttons_list
                                           ])
    )


def clicked(update, context):
    context.bot.send_message(chat_id=update.callback_query.from_user.id,

                             text='you clicked 1st button')

def number_from_user(update, context):
    pass
