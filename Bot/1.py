from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import time
import telegram
import pickle



def start(update, context):
    name = update.message.from_user.first_name
    context.bot.send_message(chat_id=update.message.chat_id,
                             text='Хеллоуууу!' + name)
    time.sleep(5)



def bye(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text='Пока - пока)')

def hello(update,context):
    file = open('d.txt', 'rb')
    users_copy = pickle.load(file)
    print(users_copy)
    file.close()

    file = open('d.txt', 'wb')
    users_copy = pickle.load(file)
    users_copy.append(input('Введите ваше имя:'))
    pickle.dump(users_copy, file)
    print(users_copy)
    file.close()

    chat_id = update.message.chat_id
    context.bot.send_chat_action(chat_id=chat_id,
                                 action=telegram.ChatAction.TYPING)
    time.sleep(5)
    if update.message.text == 'привет':
        context.bot.send_message(chat_id, text='Привет')
    if update.message.text == 'пока':
        context.bot.send_message(chat_id, text='Пока')
    if update.message.text == 'buttons':
        buttons(update, context)
    if update.message.text == 'pic1':
        pic1(update, context)
    if update.message.text == 'pic2':
        pic2(update, context)
    if update.message.text == 'pic3':
        pic3(update, context)

def buttons(update, context):
    chat_id = update.message.chat_id
    top_buttons_list = [
        InlineKeyboardButton(text='pic1', callback_data='clicked'),
        InlineKeyboardButton(text='pic2', callback_data='clicked')
    ]
    down_buttons_list = [InlineKeyboardButton(text='pic3', callback_data='clicked')]
    print(chat_id, 'clicked!')

    context.bot.send_message(
        text='Choose button:',
        chat_id=chat_id,
        reply_markup=InlineKeyboardMarkup([top_buttons_list,
                                           down_buttons_list,
                                           ])
    )

def pic1(update, context):
    context.bot.send_photo(chat_id=update.callback_query.from_user.id,
                           photo='https://images.app.goo.gl/NXehqiW5C3Xsm89K7',
                           caption='Первое фото')
def pic2(update, context):
    context.bot.send_photo(chat_id=update.callback_query.from_user.id,
                           photo='https://images.app.goo.gl/cyhoYTLwpb77cjmC9',
                           caption='Фотик намбр 2')
def pic3(update, context):
    context.bot.send_photo(chat_id=update.callback_query.from_user.id,
                           photo='https://images.app.goo.gl/fri3w6uqeJE4fADn6',
                           caption='Ласт фото')
def clicked(update, context):
    context.bot.send_message(chat_id=update.callback_query.from_user.id,
                             text='you clicked 1st button')

TOKEN = '1444025910:AAHm7cY9JTtvh_O7Unx2-pvCcP7MosMUB6w'
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('bye', bye))
dispatcher.add_handler(CallbackQueryHandler(pattern='clicked', callback=clicked))
dispatcher.add_handler(CallbackQueryHandler(pattern='pic1', callback=pic1))
dispatcher.add_handler(CallbackQueryHandler(pattern='pic2', callback=pic2))
dispatcher.add_handler(CallbackQueryHandler(pattern='pic3', callback=pic3))
dispatcher.add_handler(MessageHandler(Filters.text, hello))
updater.start_polling(clean=True)
updater.idle()
