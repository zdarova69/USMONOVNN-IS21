import json
import telebot
from telebot import types
import os
from collections import Counter
import re
import random as rn

class MyBot:
    def __init__(self):
        self.token = "2124988062:AAFPpqVZjYT9FnKaT8rPYzyUABrLBJw6XHE"
        self.bot = telebot.TeleBot(self.token)

        self.count = 0

        self.greeting_list = r"\b(Прив|Здравст|Здар|Hello|Hi)\w*\b"
        self.farewell_list =  r"\b(Пока|Прощ|bye|Досвид)\w*\b"

        self.markup1 = types.InlineKeyboardMarkup(row_width=2)
        self.item0 = types.InlineKeyboardButton(text="игра", callback_data="имя")
        self.item1 = types.InlineKeyboardButton(text="текст", callback_data="хобби")
        self.item2 = types.InlineKeyboardButton(text="фото", callback_data="возраст")
        self.item3 = types.InlineKeyboardButton(text="стикер", callback_data="жим лежа")     

        self.kb = self.markup1.add(self.item0, self.item1, self.item2, self.item3)

        self.markup_menu = types.ReplyKeyboardMarkup(row_width=2)
        
        self.btn1 = types.KeyboardButton(text='1')
        self.btn2 = types.KeyboardButton(text='2')
        self.btn3 = types.KeyboardButton(text='3')      
        self.btn4 = types.KeyboardButton(text='4')
        self.btn5 = types.KeyboardButton(text='5')      
        self.btn6 = types.KeyboardButton(text='6')

        self.markup_menu.add(self.btn1,self.btn2,self.btn3,self.btn4, self.btn5,self.btn6)
        

        self.a = [1,2,3,4,5,6]
        self.b = rn.choice(self.a)
        print(self.b)

    def run(self):
        @self.bot.message_handler(commands=['game'])
        def game(message):
            self.bot.reply_to(message, 'Давай поиграем в игру - русская рулетка. Выбери число от 1 до 6 - если не повезет - ты умрешь', reply_markup=self.markup_menu)
        @self.bot.message_handler(content_types=['sticker'])
        def uaaaa(message):
            self.bot.send_sticker(message.chat.id, sticker='CAACAgIAAxkBAAEDoBRl1OFpUBsuRXQ098-xnTztGiWznAACYw4AAsGPOUgDr1wPVUikVzQE')
        @self.bot.message_handler(commands=['photo'])
        def send_my_photo(message):
            photo = open('789.jpg', 'rb')
            self.bot.send_photo(message.chat.id, photo, 'это ты')
        @self.bot.message_handler(commands=['text'])
        def send_my_photo(message):
            file_name = message.from_user.id

            with open(str(file_name) + '.txt', 'w', encoding='utf-8') as file:
                file.write(str(message))

            with open(str(file_name) + '.txt', 'r', encoding='utf-8') as file_to_write:
                self.bot.send_document(message.chat.id, file_to_write, caption='Это твои данные')
            
        @self.bot.message_handler(commands=['start'])
        def welcome(message):
            
            self.bot.reply_to(message, "Привет! Я бот кода будузего 🤡.. Я могу сыграть с тобой в русскую рулетку. Могу отправлять тебе текстовые файлы при помощи команды /text. могу отправить фото при помощи команды /photo", reply_markup=self.kb)

                
        @self.bot.message_handler(content_types=['text'])
        def regex_answer(message):
            
            
            matches = re.findall(self.greeting_list, message.text, flags=re.IGNORECASE)
            if len(matches) >= 1:
                self.bot.reply_to(message, 'Привет')
            
            matches = re.findall(self.farewell_list, message.text, flags=re.IGNORECASE)
            if len(matches) >= 1:
                self.bot.reply_to(message, 'Пока')
            
            print(type(message.text))
            if message.text == str(self.b):
                print('ты умер')
                self.bot.reply_to(message, 'Ты умер')
            else:
                pass

        
        #работа с json
        @self.bot.callback_query_handler(func=lambda call: True)
        def callback_inline(call):
            if call.data == "имя":
                self.bot.send_message(call.message.chat.id, f" могу сыграть с тобой в русскую рулетку, отправь мне /game")

            elif call.data == "хобби":
                self.bot.send_message(call.message.chat.id, f" могу отправить тебе текстовый файл,отправь мне /text")

            elif call.data == "возраст":
                self.bot.send_message(call.message.chat.id, f"  могу отправить фото при помощи команды /photo")

            elif call.data == "жим лежа":
                self.bot.send_message(call.message.chat.id, f" могу отправить тебе стикер,отправь мне его в ответ")

   
        self.bot.polling(none_stop=True)

if __name__ == '__main__':
    my_bot = MyBot()
    my_bot.run()
