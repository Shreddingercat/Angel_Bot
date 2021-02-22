# -*- coding: utf8 -*-

import Token
import Text_Instruction

import telebot
bot = telebot.TeleBot(Token.token)

from telebot import types

welcome_text = Text_Instruction.welcome
missing_instruction = Text_Instruction.missing
found_instruction = Text_Instruction.found
volunteer_instruction = Text_Instruction.volunteer
donate_instruction = Text_Instruction.donate

@bot.message_handler(content_types=['text'])
def start_message(message):
    if message.text == '/start':
        keyboard = types.InlineKeyboardMarkup()
        key_missing = types.InlineKeyboardButton(text='Пропал человек', callback_data='missing')
        keyboard.add(key_missing)
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