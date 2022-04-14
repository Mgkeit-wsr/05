import telebot
from check import check
# Тема : Поиск работы для молодых профессионалов Москвы
job_app = []
bot = telebot.TeleBot('5377628865:AAFceGMbzqVV7PduGB-IBjilgDCJAzIzha0')

markup = telebot.types.ReplyKeyboardRemove(selective=False)


@bot.message_handler(commands=['start'])
def start(message, res=False):
    markup0 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_message(message.chat.id, 'Привет! Я ProfBotik. :D')
    item1 = telebot.types.KeyboardButton('Несовершеннолетний')
    item2 = telebot.types.KeyboardButton('Совершеннолетний')
    markup0.add(item1)
    markup0.add(item2)
    bot.send_message(message.chat.id, 'Вы совершеннолетний?', reply_markup=markup0)

@bot.message_handler(content_types=['text'])
def age_check(message):
    if message.text.strip() == 'Несовершеннолетний':
      job_app.append('Несовершеннолетний')
      bot.send_message(message.chat.id, 'Учтено')
    elif message.text.strip() == 'Совершеннолетний':
      job_app.append('Совершеннолетний')
      bot.send_message(message.chat.id, 'Учтено')

@bot.message_handler(content_types=['text'])
def podrabotka(message,res = False):
    markup1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton('Подработка')
    item2 = telebot.types.KeyboardButton('Постоянная')
    markup1.add(item1)
    markup1.add(item2)
    bot.send_message(message.chat.id, 'На какой основе хотите работать?', reply_markup=markup1)

@bot.message_handler(content_types=['text'])
def podrabotka_check(message):
    if message.text.strip() == 'Подработка':
        job_app.append('Подработка')
        bot.send_message(message.chat.id, 'Учтено')
    elif message.text.strip() == 'Постоянная':
        job_app.append('Постоянная')
        bot.send_message(message.chat.id, 'Учтено')

@bot.message_handler(content_types=['text'])
def quality_check(message,res = True):
    bot.send_message(message.chat.id, 'Напишите про вашу квалификацию. Например: программист.')
    try:
        user_input2 = str(message.text)
    except:
        bot.send_message(message.chat.id, 'Попробуйте еще раз')
    else:
        job_app.append(user_input2)
        bot.send_message(message.chat.id, 'Учтено')
      
@bot.message_handler(content_types=['text'])
def result(message):
  bot.send_message(message.chat.id, str(job_app) + '\n' + 'Вам больше всего подходит:'  + check(job_app[3]))
  
bot.polling(none_stop=True, interval=0)
