# -*- coding: utf8 -*-

import Token

import telebot
bot = telebot.TeleBot(Token.token)

from telebot import types

welcome_text = 'Здравствуйте! Это telegram-бот поисково-спасательного отряда "Ангел". Поисково-спасательный отряд ' \
               '«Ангел» - первое в Республике Беларусь добровольное движение по оказанию помощи в поиске без вести ' \
               'пропавших людей. Чем мы можем Вам помочь?'
missing_instruction = 'Если пропал человек, в первую очередь следует позвонить в Бюро регистрации несчастных случаев ' \
                      '(БРНС) (номера телефонов смотреть ниже). Вся информация ежесуточно стекает сюда из дежурных ' \
                      'частей ОВД, вытрезвителей, больниц и моргов, и заносится в единую базу данных. Здесь ' \
                      'находятся сведения о лицах, задержанных органами внутренних дел, и лицах, доставленных в ' \
                      'медицинские учреждения, не имеющих возможности сообщить о себе сведения, а также и информация ' \
                      'об обнаружении неизвестных трупов. Вам необходимо подробно рассказать оператору о произошедшем' \
                      '. Там Вам дадут информацию о всех несчастных случаях и ДТП, произошедших за минувшие сутки. ' \
                      'Следует проверить факт возможной госпитализации пропавшего человека службой скорой помощи.'
found_instruction = 'Позвоните по любому из номеров, указанных в ориентировке.'
volunteer_instruction = 'Лично Вы можете помочь в поиске пропавшего:\n- распространением информации в интернете;\n' \
                        '- расклейкой ориентировок и опросом прохожих;\n- выездом на городские и лесные поиски;\n' \
                        '- и другим (доп. информация на стене группы).\n\nКаждый человек независимо от того, в каком ' \
                        'городе он находится, может оказать существенную помощь. Нам дорог каждый!'
donate_instruction = 'Как можно поддержать ПСО "Ангел"?\nС помощью пожертвований!\n\n☎ USSD-запрос для абонентов МТС' \
                     ', А1 и life:) - *222*13#!\n💳 переводом с банковской карточки (есть также и подписка на ' \
                     'ежемесячные перечисления) https://imenamag.by/projects/26988691\n📥 Электронные платежи (ЕРИП) ' \
                     'код услуги 4345671\n☎ пополнение отрядных моб.телефонов 8 (033) 6666-856, 8 (033) 6666-033'

@bot.message_handler(content_types=['text'])
def start_message(message):
    if message.text == '/start':
        keyboard = types.InlineKeyboardMarkup() #клавиатура
        key_missing = types.InlineKeyboardButton(text='Пропал человек', callback_data='missing')
        keyboard.add(key_missing) #добавляем кнопку в клавиатуру
        key_found = types.InlineKeyboardButton(text='Найден человек', callback_data='found')
        keyboard.add(key_found)
        key_volunteer = types.InlineKeyboardButton(text='Хочу стать волонтером', callback_data='volunteer')
        keyboard.add(key_volunteer)
        key_donate = types.InlineKeyboardButton(text='Оказать материальную помощь', callback_data='donate')
        keyboard.add(key_donate)
        bot.send_message(message.from_user.id, text=welcome_text, reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, text='Ваше сообщение принято. Мы свяжемся с Вами в ближайшее время')

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'missing': #call.data это callback_data, которую мы указали при объявлении кнопки
        bot.send_message(call.message.chat.id, text=missing_instruction)
    elif call.data == 'found':
        bot.send_message(call.message.chat.id, text=found_instruction)
    elif call.data == 'volunteer':
        bot.send_message(call.message.chat.id, text=volunteer_instruction)
    elif call.data == 'donate':
        bot.send_message(call.message.chat.id, text=donate_instruction)

bot.polling(none_stop=True, interval=0)