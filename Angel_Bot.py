#!/usr/bin/python3.8
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

keyboard = types.InlineKeyboardMarkup()
key_missing = types.InlineKeyboardButton(text=Text_Instruction.missing_key, callback_data='missing')
keyboard.add(key_missing)
key_found = types.InlineKeyboardButton(text=Text_Instruction.found_key, callback_data='found')
keyboard.add(key_found)
key_volunteer = types.InlineKeyboardButton(text=Text_Instruction.volunteer_key, callback_data='volunteer')
keyboard.add(key_volunteer)
key_donate = types.InlineKeyboardButton(text=Text_Instruction.donate_key, callback_data='donate')
keyboard.add(key_donate)

@bot.message_handler(content_types=['text'])
def start_message(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, text=welcome_text, reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, text=Text_Instruction.feedback, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'missing':
        bot.send_message(call.message.chat.id, text=missing_instruction, reply_markup=keyboard)
    elif call.data == 'found':
        bot.send_message(call.message.chat.id, text=found_instruction, reply_markup=keyboard)
    elif call.data == 'volunteer':
        bot.send_message(call.message.chat.id, text=volunteer_instruction, reply_markup=keyboard)
    elif call.data == 'donate':
        bot.send_message(call.message.chat.id, text=donate_instruction, reply_markup=keyboard)

bot.polling(none_stop=True, interval=0)