from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import sqlite3, requests
from numb import *
from crocodile import *
from fate import *
def start(update, context):
    name = update.message.from_user.first_name
    id = update.message.chat_id
    context.bot.send_message(chat_id=update.message.chat_id,
                             text='Хеллооууу ')
    context.bot.send_message(chat_id=update.message.chat_id,
                             text=start_msg)
    conn = sqlite3.connect('base/data.sqlite')
    cursor = conn.cursor()

    user_exists = cursor.execute('''
    select id
    from NewUsers
    where id= '{}'
    '''.format(id)).fetchall()

    if len(user_exists) != 0:
        cursor.execute('''
        insert into NewUsers values('{}', '{}','{}', '{}')
        '''.format(id, name, random.randint(1000, 10000)))
        conn.commit()

def text(update, context):
    s = ''
    if update.message.text.isalnum and len(update.message.text) == 12:
        URL = 'https://api.tehnikum.school/sms/sms.php'
        conn = sqlite3.connect('base/data.sqlite')
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

    context.bot.send_message(chat_id=update.message.chat_id,
                             text='Введите код')
    if update.message.text.isalnum and len(update.message.text) == 4:
        conn = sqlite3.connect('base/data.sqlite')
        cursor = conn.cursor()
        id = update.message.chat_id

        user_code = cursor.execute('''
            select code
            from NewUsers
            where id= '{}'
            '''.format(id)).fetchall()[0][0]

        if int(update.message.text) == int(user_code):
            context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
            time.sleep(2)
            context.bot.send_message(chat_id=id, text='Правильно!')
        else:
            context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
            time.sleep(2)
            context.bot.send_message(chat_id=id, text='Проверьте ваш код...')



    context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    time.sleep(3)
    context.bot.send_message(chat_id=update.message.chat_id,
                             text=tnk)
    context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    time.sleep(2)
    context.bot.send_message(chat_id=update.message.chat_id,
                             text=first)
    context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    time.sleep(5)
    context.bot.send_message(chat_id=update.message.chat_id,
                                 text=intro)
    chat_id = update.message.chat_id
    buttons_list = [
        InlineKeyboardButton(text='Кроко', callback_data=croco(update, context)),
        InlineKeyboardButton(text='Отгадай число', callback_data=numb(update, context)),
        InlineKeyboardButton(text='Послание из будущего', callback_data=fate(update, context))
    ]
    print(chat_id, 'clicked')

    context.bot.send_message(
        text='Choose button:',
        chat_id=chat_id,
        reply_markup=InlineKeyboardMarkup([buttons_list
                                           ])
    )

def clicked(update, context):
    context.bot.send_message(chat_id=update.callback_query.from_user.id,

                             text='you clicked 1st button')
