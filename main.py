import telebot 
# Тема : Поиск работы для молодых профессионалов Москвы
job_app = []
bot = telebot.TeleBot('5377628865:AAFceGMbzqVV7PduGB-IBjilgDCJAzIzha0')

markup = telebot.types.ReplyKeyboardRemove(selective=False)
def sep(text):
  return text
def check(prof_name):
  my_file=open('work.txt','r')
  for line in my_file:
    line_temp = line.split('+')
    prof_in_file = line_temp[1]
    if prof_in_file[:-1]== prof_name:
      return line_temp[0]
  return 'Ничего не найдено, попробуйте ещё раз.'

@bot.message_handler(commands=['start'])
def start(message, res=False):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_message(message.chat.id, 'Привет! Я ProfBotik. :D')
    item1 = telebot.types.KeyboardButton('Несовершеннолетний')
    item2 = telebot.types.KeyboardButton('Совершеннолетний')
    markup.add(item1)
    markup.add(item2)
    bot.send_message(message.chat.id, 'Вы совершеннолетний?', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def main(message):
    if message.text.strip() == 'Несовершеннолетний':
      bot.send_message(message.chat.id, 'Учтено и отклонено')
    elif message.text.strip() == 'Совершеннолетний':
      bot.send_message(message.chat.id, 'Учтено')
      markup =telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
      item1 = telebot.types.KeyboardButton('Подработка')
      item2 = telebot.types.KeyboardButton('Постоянная')
      markup.add(item1)
      markup.add(item2)
      bot.send_message(message.chat.id, 'На какой основе хотите работать?', reply_markup=markup)
    if message.text.strip() == 'Подработка':
      bot.send_message(message.chat.id, 'Учтено')
      bot.send_message(message.chat.id, 'Напишите про вашу квалификацию. Например: Безопасность. (с большой буквы!)')
      lastMessageId = message[-1].messsage_id
      lastChatId = message[-1].chat.id
      user_input2 = sep(message.text)
      job_app.append(user_input2)
      bot.send_message(message.chat.id, 'Учтено')
      bot.send_message(message.chat.id, '\n' + 'Вам больше всего подходит:'  + check(job_app[0]))
    elif message.text.strip() == 'Постоянная':
      bot.send_message(message.chat.id, 'Учтено')
      bot.send_message(message.chat.id, 'Напишите про вашу квалификацию. Например: Безопасность. (с большой буквы!)')
      user_input2 = sep(message.text)
      job_app.append(user_input2)
      bot.send_message(message.chat.id, 'Учтено',job_app[0])
      bot.send_message(message.chat.id, '\n' + 'Вам больше всего подходит:'  + check(job_app[0]))

bot.polling(none_stop=True, interval=0)