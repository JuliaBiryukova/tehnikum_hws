from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from functions import *


updater = Updater(token=TOKEN, workers=30)

dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))

dispatcher.add_handler(CallbackQueryHandler(pattern='contact', callback=contact))
dispatcher.add_handler(CallbackQueryHandler(pattern='cro', callback=cro))
dispatcher.add_handler(CallbackQueryHandler(pattern='numb', callback=numb))
dispatcher.add_handler(CallbackQueryHandler(pattern='fate', callback=fate))

dispatcher.add_handler(CallbackQueryHandler(pattern='cro_butt', callback=cro_butt))
dispatcher.add_handler(CallbackQueryHandler(pattern='qsn1', callback=qsn1))
dispatcher.add_handler(CallbackQueryHandler(pattern='qsn2', callback=qsn2))
dispatcher.add_handler(CallbackQueryHandler(pattern='qsn3', callback=qsn3))
dispatcher.add_handler(CallbackQueryHandler(pattern='qsn4', callback=qsn4))
dispatcher.add_handler(CallbackQueryHandler(pattern='qsn5', callback=qsn5))
dispatcher.add_handler(CallbackQueryHandler(pattern='qsn6', callback=qsn6))
dispatcher.add_handler(CallbackQueryHandler(pattern='qsn7', callback=qsn7))

dispatcher.add_handler(CallbackQueryHandler(pattern='rght', callback=rght))
dispatcher.add_handler(CallbackQueryHandler(pattern='wrn', callback=wrng))
dispatcher.add_handler(CallbackQueryHandler(pattern='dknw', callback=dknw))

dispatcher.add_handler(CallbackQueryHandler(pattern='poslaniye', callback=poslaniye))


updater.start_polling(clean=True)
updater.idle()
