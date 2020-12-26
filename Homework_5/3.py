from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram.ext import Filters

eng_dic = {'Hi': 'Hi! How are you?',
            'Hello': 'Hi! How are you?',
           'Great': '<3',
           'Good': 'great',
           'Not bad': 'Good!',
           'Add user': 'We added you to the list',
           'Deluser': 'We strangled you off the list',
           'Bye': 'Bye-Bye'}

rus_dic = {'привет': 'Привет, как ты?',
           'првет': 'Привет, как ты?',
           'прив': 'Привет,как ты?',
           'Приветик': 'Привет,как ты?',
           'Хорошо': 'хорошо',
           'Добавить пользователя': 'Мы добавили вас в список',
           'Пока': 'Досвидули <3'}

uzb_dic = {'Salom': 'Salom, qandisan?',
           'Yaxshi': '<3',
           "qo'yhatga qo'shish": "siz ro'yhatga qo'shildiz",
           "ro'yhatdan o'chirish": "siz ro'yhatdan o'chirildiz",
           'hayr': 'Xayr',
           'Xayr': 'Xayr'}

def start(update, context):
    name = update.message.from_user.username
    context.bot.send_message(chat_id=update.message.chat_id,
                             text='Хеллоооу!' + name)

def adduser(update, context):
    l = open('text.txt', 'a')
    name = update.message.from_user.first_name
    l.write(name + '\n')
    if update.message.text in eng_dic.keys():
        context.bot.send_message(chat_id=update.message.chat_id, text=eng_dic[update.message.text][1])
    elif update.message.text in rus_dic.keys():
        context.bot.send_message(chat_id=update.message.chat_id, text=rus_dic[update.message.text][1])
    elif update.message.text in uzb_dic.keys():
        context.bot.send_message(chat_id=update.message.chat_id, text=uzb_dic[update.message.text][1])

def deluser(update, context):
    n = []
    x = ()
    l = open('text.txt', 'r')
    for i in l:
        n.append(i)
        x = str(i)
    n.remove(x)
    l.close()
    l = open('text.txt', 'w')
    for i in n:
        l.write(i)
        l.close()
    if update.message.text in eng_dic.keys():
        context.bot.send_message(chat_id=update.message.chat_id, text=eng_dic[update.message.text][1])
    elif update.message.text in rus_dic.keys():
        context.bot.send_message(chat_id=update.message.chat_id, text=rus_dic[update.message.text][1])
    elif update.message.text in uzb_dic.keys():
        context.bot.send_message(chat_id=update.message.chat_id, text=uzb_dic[update.message.text][1])

def bye(update, context):
    if update.message.text in eng_dic.keys():
        context.bot.send_message(chat_id=update.message.chat_id, text=eng_dic[update.message.text][1])
    elif update.message.text in rus_dic.keys():
        context.bot.send_message(chat_id=update.message.chat_id, text=rus_dic[update.message.text][1])
    elif update.message.text in uzb_dic.keys():
        context.bot.send_message(chat_id=update.message.chat_id, text=uzb_dic[update.message.text][1])

TOKEN = '1484337650:AAHdJm-3CZRmb23MM5F4L5l6KrNL12hOleo'
updater = Updater(token=TOKEN)


dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('bye', bye))
dispatcher.add_handler(MessageHandler(Filters.text, adduser))
dispatcher.add_handler(MessageHandler(Filters.text, deluser))

updater.start_polling(clean=True)
updater.idle()
