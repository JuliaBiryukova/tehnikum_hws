from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from functions import *
from crocodile import *

updater = Updater(token=TOKEN)

dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(Filters.text, text))
dispatcher.add_handler(CallbackQueryHandler(pattern='clicked', callback=clicked))
updater.start_polling(clean=True)
updater.idle()
