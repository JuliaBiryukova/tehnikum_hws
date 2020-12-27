from telegram.ext import Updater, CommandHandler


def start(update, context):
    name = update.message.from_user.first_name
    context.bot.send_message(chat_id=update.message.chat_id,
                             text='Хеллоооу!' + name)

def add(update, context):
    l = open('text.txt', 'a')
    name = update.message.from_user.first_name
    l.write(name + '\n')
    context.bot.add_user(chat_id=update.message.chat_id, text='Мы добавили вас в список')


def delite(update, context):
    name = update.message.from_user.first_name
    n = []
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
    context.bot.send_message(chat_id=update.message.chat_id, text='Вы были удалены из списка')


def bye(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text = 'Досвидули <3')


TOKEN = '1484306825:AAEUjpOuGHe7dAqGvT166U3jppMPCL2e60k'

updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('adduser', add))
dispatcher.add_handler(CommandHandler('deluser', delite))
dispatcher.add_handler(CommandHandler('bye', bye))

updater.start_polling(clean=True)
updater.idle()
