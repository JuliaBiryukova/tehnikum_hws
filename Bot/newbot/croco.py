context.bot.send_message(chat_id=update.message.chat_id,
                             text=qtn5)
    
    while True:
        if update.message.text == 'повеситься':
            context.bot.send_message(chat_id=update.message.chat_id,
                                 text=ans1)
        else:
            context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
            time.sleep(2)
            context.bot.send_message(chat_id=update.message.chat_id,
                             text=ans)
    time.sleep(2)



    context.bot.send_message(chat_id=update.message.chat_id,
                             text=qtn6)
    
    while True:
        if update.message.text == 'кондуктор':
            context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
            time.sleep(3)
            context.bot.send_message(chat_id=update.message.chat_id,
                                 text=ans1)
        else:
            context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
            time.sleep(2)
            context.bot.send_message(chat_id=update.message.chat_id,
                             text='Кондуктор')
    time.sleep(2)
    c



    context.bot.send_message(chat_id=update.message.chat_id,
                             text=qtn7)
    
    while True:
        if update.message.text == 'таракан':
            context.bot.send_message(chat_id=update.message.chat_id,
                                 text='Сразу видно что ты услышал про своих')
        else:
            context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
            time.sleep(2)
            context.bot.send_message(chat_id=update.message.chat_id,
                             text='Таракан! Это был Таракан!')
    time.sleep(2)




    context.bot.send_message(chat_id=update.message.chat_id,
                             text=qtn8)
    
    while True:
        if update.message.text == 'спичку':
            context.bot.send_message(chat_id=update.message.chat_id,
                                 text=ans1)
        else:
            context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
            time.sleep(2)
            context.bot.send_message(chat_id=update.message.chat_id,
                             text='Эх, это была спичка. Ну ты даун:)')

    context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    time.sleep(2)
    context.bot.send_message(chat_id=update.message.chat_id, text='Молодец, Рад был с тобой поиграть')
    chat_id = update.message.chat_id
    button_list = [
        KeyboardButton(text='Продолжить игру', callback_data='clicked'),
        KeyboardButton(text='Вернуться', callback_data=buttons_list)
    ]
    print(chat_id, 'clicked')

    context.bot.send_message(
        text='Choose button:',
        chat_id=chat_id,
        reply_markup=ReplyKeyboardMarkup([button_list
                                          ])
    )
