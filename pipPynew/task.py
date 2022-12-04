import telebot
#Создадим ссылку на бота
bot = telebot.TeleBot('Your Token', parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
markup.row("/registration", "/help")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, "Choose command:", reply_markup=markup)

@bot.message_handler(commands=['registration'])
def registr(message):
    data = str(message.from_user.id)+ '\n'
    with open('log_id.txt', 'r+', encoding='utf-8') as f:
        text_id = f.readlines()
        if data not in text_id:
            f.writelines(data)
            bot.reply_to(message, "Регистрация прошла успешно")
        else:
            bot.reply_to(message, "Ваша запись уже зарегистрирована")

@bot.message_handler(commands=['help'])#когда сообщение придет бот сам об этом скажет
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(content_types=["text", "sticker"])
def function_name(message):
    with open('mess.txt', 'a', encoding='utf-8') as data:
        data.writelines(message.text+'\n')
    #bot.reply_to(message, "This is a message handler")
    text = message.text
    if "привет" in text.lower():
        bot.reply_to(message, f"Привет, {message.from_user.first_name}!")

# #запуск бота на постоянную(бесконечную) работу
# bot.infinity_polling()
bot.polling(none_stop =True, interval=0) #interval = 1 - задержка в ответе бота 1 сек

