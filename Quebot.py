import telebot
from telebot import types
import random

bot = telebot.TeleBot("5793554451:AAFGt7qnaAxKfKvQq6SBGxBxH4FY6YMi8Xk")
points = 0

words1 = ['Ответ правильный!', 'Молодец!', 'Так держать!', 'Продолжай в том же духе!']
random1 = random.choises(words1)
random2 = random1[0] or random1[1] or random1[2] or random1[3]

words2 = ['Ответ Не правильный', 'К сожелению у тебя не правильно!', 'У тебя не получилось!', 'Нужно еще немного подучить!']
random1 = random.choises(words2)
random2 = random1[0] or random1[1] or random1[2] or random1[3]


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет')


@bot.message_handler(content_types=['photo'])
def question(message):
    global points
    global random1
    global random2
    if message.text == "quiz" or message.text == "quiz":
        points = 0
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_wids=4)
        item1 = types.KeyboardButton('July')
        item2 = types.KeyboardButton('June')
        item3 = types.KeyboardButton('May')
        item4 = types.KeyboardButton('September')
        markup.add(item1, item2, item3, item4)
        bot.send_message(message.chat.id, '1. ..... is the first mounts is summer in Russia.', reply_markup=markup)

    if message.chat.type == 'private':
        if message.text == 'June':
            bot.send_message(message.chat.id, random1)
            points += 1

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_wids=4)
            item1 = types.KeyboardButton('Did...spend')
            item2 = types.KeyboardButton('Do...spend')
            item3 = types.KeyboardButton('Did...spent')
            item4 = types.KeyboardButton('Do...spent')
            markup.add(item1, item2, item3, item4)
            bot.send_message(message.chat.id, '2. ..... you .... last summer at the seaside?', reply_markup=markup)

        else:
            bot.send_message(message.chat.id, random2)
            bot.send_message(message.chat.id, 'Ответ: June')
            points += 0

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_wids=4)
            item1 = types.KeyboardButton('Did...spend')
            item2 = types.KeyboardButton('Do...spend')
            item3 = types.KeyboardButton('Did...spent')
            item4 = types.KeyboardButton('Do...spent')
            markup.add(item1, item2, item3, item4)
            bot.send_message(message.chat.id, '2. ..... you .... last summer at the seaside?', reply_markup=markup)


        if message.text == 'Did...spend':
            bot.send_message(message.chat.id, random1)
            points += 1

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_wids=4)
            item1 = types.KeyboardButton('is packing')
            item2 = types.KeyboardButton('packs')
            item3 = types.KeyboardButton('packed')
            item4 = types.KeyboardButton('pack')
            markup.add(item1, item2, item3, item4)
            bot.send_message(message.chat.id, '3. Marry .... her school bug now.', reply_markup=markup)

        else:
            bot.send_message(message.chat.id, random2)
            bot.send_message(message.chat.id, 'Ответ: Did...spend')
            points += 0

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_wids=4)
            item1 = types.KeyboardButton('is packing')
            item2 = types.KeyboardButton('packs')
            item3 = types.KeyboardButton('packed')
            item4 = types.KeyboardButton('pack')
            markup.add(item1, item2, item3, item4)
            bot.send_message(message.chat.id, '3. Marry .... her school bug now.', reply_markup=markup)


        if message.text == 'packs':
            bot.send_message(message.chat.id, random1)
            points += 1

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_wids=4)
            item1 = types.KeyboardButton('in front')
            item2 = types.KeyboardButton('to the left')
            item3 = types.KeyboardButton('between')
            item4 = types.KeyboardButton('in back')
            markup.add(item1, item2, item3, item4)
            bot.send_message(message.chat.id, '4. There is cafe .... the cinema and the bank.', reply_markup=markup)

        else:
            bot.send_message(message.chat.id, random2)
            bot.send_message(message.chat.id, 'Ответ: packs')
            points += 0

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_wids=4)
            item1 = types.KeyboardButton('in front')
            item2 = types.KeyboardButton('to the left')
            item3 = types.KeyboardButton('between')
            item4 = types.KeyboardButton('in back')
            markup.add(item1, item2, item3, item4)
            bot.send_message(message.chat.id, '4. There is cafe .... the cinema and the bank.', reply_markup=markup)


        if message.text == 'between':
            bot.send_message(message.chat.id, random1)
            points += 1

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_wids=4)
            item1 = types.KeyboardButton('where')
            item2 = types.KeyboardButton('was')
            item3 = types.KeyboardButton('is')
            item4 = types.KeyboardButton('in')
            markup.add(item1, item2, item3, item4)
            bot.send_message(message.chat.id, '5. There .... a museum and a theatre in this square last year.', reply_markup=markup)

        else:
            bot.send_message(message.chat.id, random2)
            bot.send_message(message.chat.id, 'Ответ: between')
            points += 0

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_wids=4)
            item1 = types.KeyboardButton('where')
            item2 = types.KeyboardButton('was')
            item3 = types.KeyboardButton('is')
            item4 = types.KeyboardButton('in')
            markup.add(item1, item2, item3, item4)
            bot.send_message(message.chat.id, '5. There .... a museum and a theatre in this square last year.', reply_markup=markup)

        if message.text == 'is':
            bot.send_message(message.chat.id, random1)
            points += 1

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_wids=4)
            item1 = types.KeyboardButton('to')
            item2 = types.KeyboardButton('in')
            item3 = types.KeyboardButton('for')
            item4 = types.KeyboardButton('on')
            markup.add(item1, item2, item3, item4)
            bot.send_message(message.chat.id, '6. They left Paris .... Moscow two days ago.',
            reply_markup=markup)

        else:
            bot.send_message(message.chat.id, random2)
            bot.send_message(message.chat.id, 'Ответ: is')
            points += 0

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_wids=4)
            item1 = types.KeyboardButton('to')
            item2 = types.KeyboardButton('in')
            item3 = types.KeyboardButton('for')
            item4 = types.KeyboardButton('on')
            markup.add(item1, item2, item3, item4)
            bot.send_message(message.chat.id, '6. They left Paris .... Moscow two days ago.',
            reply_markup=markup)


        if message.text == 'to':
            bot.send_message(message.chat.id, random1)
            points += 1

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_wids=4)
            item1 = types.KeyboardButton('any')
            item2 = types.KeyboardButton('some')
            item3 = types.KeyboardButton('much')
            item4 = types.KeyboardButton('many')
            markup.add(item1, item2, item3, item4)
            bot.send_message(message.chat.id, "7. There aren't ... apples at home. Can you buy some?",
            reply_markup=markup)

        else:
            bot.send_message(message.chat.id, random2)
            bot.send_message(message.chat.id, 'Ответ: to')
            points += 0

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_wids=4)
            item1 = types.KeyboardButton('any')
            item2 = types.KeyboardButton('some')
            item3 = types.KeyboardButton('much')
            item4 = types.KeyboardButton('many')
            markup.add(item1, item2, item3, item4)
            bot.send_message(message.chat.id, "7. There aren't ... apples at home. Can you buy some?",
            reply_markup=markup)

        if message.text == 'much':
            bot.send_message(message.chat.id, random1)
            points += 1

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_wids=4)
            item1 = types.KeyboardButton('some')
            item2 = types.KeyboardButton('any')
            item3 = types.KeyboardButton('many')
            item4 = types.KeyboardButton('more')
            markup.add(item1, item2, item3, item4)
            bot.send_message(message.chat.id, "8. Is there .... cheese in the fridge?",
                             reply_markup=markup)

        else:
            bot.send_message(message.chat.id, random2)
            bot.send_message(message.chat.id, 'Ответ: much')
            points += 0

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_wids=4)
            item1 = types.KeyboardButton('some')
            item2 = types.KeyboardButton('any')
            item3 = types.KeyboardButton('many')
            item4 = types.KeyboardButton('more')
            markup.add(item1, item2, item3, item4)
            bot.send_message(message.chat.id, "8. Is there .... cheese in the fridge?",
                             reply_markup=markup)


        if message.text == 'many':
            bot.send_message(message.chat.id, random1)
            points += 1

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_wids=4)
            item1 = types.KeyboardButton('Do')
            item2 = types.KeyboardButton('Does')
            item3 = types.KeyboardButton('Is')
            item4 = types.KeyboardButton('Did')
            markup.add(item1, item2, item3, item4)
            bot.send_message(message.chat.id, "9. .... your Granny usually cook pancakes at the weekend.",
                             reply_markup=markup)

        else:
            bot.send_message(message.chat.id, random2)
            bot.send_message(message.chat.id, 'Ответ: many')
            points += 0

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_wids=4)
            item1 = types.KeyboardButton('Do')
            item2 = types.KeyboardButton('Does')
            item3 = types.KeyboardButton('Is')
            item4 = types.KeyboardButton('Did')
            markup.add(item1, item2, item3, item4)
            bot.send_message(message.chat.id, "9. .... your Granny usually cook pancakes at the weekend.",
                             reply_markup=markup)


        if message.text == 'Do':
            bot.send_message(message.chat.id, random1)
            points += 1

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_wids=4)
            item1 = types.KeyboardButton('a')
            item2 = types.KeyboardButton('the')
            item3 = types.KeyboardButton('an')
            item4 = types.KeyboardButton('on')
            markup.add(item1, item2, item3, item4)
            bot.send_message(message.chat.id, "10. There is ... armchair to the right of the window.",
                             reply_markup=markup)

        else:
            bot.send_message(message.chat.id, random2)
            bot.send_message(message.chat.id, 'Ответ: Do')
            points += 0

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_wids=4)
            item1 = types.KeyboardButton('a')
            item2 = types.KeyboardButton('the')
            item3 = types.KeyboardButton('an')
            item4 = types.KeyboardButton('on')
            markup.add(item1, item2, item3, item4)
            bot.send_message(message.chat.id, "10. There is ... armchair to the right of the window.",
                             reply_markup=markup)


        if message.text == 'a':
            bot.send_message(message.chat.id, random1)
            points += 1

            bot.send_message(message.chat.id, f"Вы набрали: {points}")

        else:
            bot.send_message(message.chat.id, random2)
            bot.send_message(message.chat.id, 'Ответ: a')
            points += 0

            bot.send_message(message.chat.id, f"Вы набрали: {points}")

bot.polling()
