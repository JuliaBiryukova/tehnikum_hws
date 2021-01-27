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
