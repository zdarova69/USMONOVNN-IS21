#импортируем библиотеки
import telebot
from telebot import types

import json
import time

import testAPI2




class MyBot:
    def __init__(self):
        #данные бота
        self.token = "6095239590:AAGLodvJdqeE7EK-dfiFtZgsr8WtSwwd1-4"
        self.bot = telebot.TeleBot(self.token)
        #получаем имя пользователя
        self.user_name = ''
        self.chat_id = ''

        #кнопки для ответов на вопросы
        self.markup1 = types.InlineKeyboardMarkup(row_width=2)
        self.item0 = types.InlineKeyboardButton(text="что такое переменная?", callback_data="переменная")
        self.item1 = types.InlineKeyboardButton(text="что такое типы данных?", callback_data="типы данных")
        self.item2 = types.InlineKeyboardButton(text="что такое условия?", callback_data="условия")
        self.item3 = types.InlineKeyboardButton(text="что такое циклы?", callback_data="циклы")
        self.item4 = types.InlineKeyboardButton(text="что такое ооп?", callback_data="ооп")
        
        self.kb = self.markup1.add(self.item0, self.item1, self.item2, self.item3, self.item4)
        
        self.markup_search = types.InlineKeyboardMarkup(row_width=1)
        self.item_result = types.InlineKeyboardButton(text="получить ответ", callback_data="ответ")
        self.kb_search = self.markup_search.add(self.item_result)
    
    #запускаем бота
    def run(self):
        print('бот запущен')
        
        @self.bot.message_handler(commands=['start'])
        def welcome(message):

            self.chat_id = message.chat.id
            self.user_name = message.from_user.first_name

            self.bot.reply_to(message, f"Привет, {self.user_name}! Я бот кода будущего. Задай мне вопрос:", reply_markup=self.kb)

        @self.bot.message_handler(commands=['search'])
        def search(message):
            request = message.text[8:]
            print(message.chat.id)
            self.chat_id = message.chat.id
            self.bot.send_message(message.chat.id, text='Бот начал поиск!')
            testAPI2.search_api(request)
            time.sleep(1)
            self.bot.send_message(message.chat.id, text='поиск закончен!', reply_markup=self.kb_search)

            
            
            
        @self.bot.callback_query_handler(func=lambda call: True)
        def callback_inline(call):
            if call.data == "переменная":
                markup = types.InlineKeyboardMarkup(row_width=2)
                markup.add(self.item1, self.item2, self.item3, self.item4)
                self.bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
                self.bot.send_message(call.message.chat.id, "Переме́нная в императивном программировании — поименованная, либо адресуемая иным способом область памяти, адрес которой можно использовать для осуществления доступа к данным. Данные, находящиеся в переменной, называются значением этой переменной.", reply_markup=markup)

            elif call.data == "типы данных":
                markup = types.InlineKeyboardMarkup(row_width=2)
                markup.add(self.item0, self.item2, self.item3, self.item4)
                self.bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
                self.bot.send_message(call.message.chat.id, "Типы данных - класс данных, характеризуемый членами класса и операциями, которые могут быть к ним применены", reply_markup=markup)

            elif call.data == "условия":
                markup = types.InlineKeyboardMarkup(row_width=2)
                markup.add(self.item0, self.item1, self.item3, self.item4)
                self.bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
                self.bot.send_message(call.message.chat.id, "Условия - выражение логического типа (Boolean), которое может принимать одно из двух значений: True (истина) или False (ложь)", reply_markup=markup)

            elif call.data == "циклы":
                markup = types.InlineKeyboardMarkup(row_width=2)
                markup.add(self.item0, self.item1, self.item2, self.item4)
                self.bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
                self.bot.send_message(call.message.chat.id, "Циклы - разновидность управляющей конструкции в высокоуровневых языках программирования, предназначенная для организации многократного исполнения набора инструкций.", reply_markup=markup)

            elif call.data == "ооп":
                markup = types.InlineKeyboardMarkup(row_width=2)
                markup.add(self.item0, self.item1, self.item2, self.item3)
                self.bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
                self.bot.send_message(call.message.chat.id, "Объе́ктно-ориенти́рованное программи́рование — методология программирования, основанная на представлении программы в виде совокупности объектов, каждый из которых является экземпляром определённого класса, а классы образуют иерархию наследования.", reply_markup=markup)
            
            elif call.data == 'ответ':
                with open('result.json', 'r') as result:
                    result = json.load(result)
                    self.bot.send_message(self.chat_id, text=result)
                    
        self.bot.polling(none_stop=True)

if __name__ == '__main__':
    my_bot = MyBot()
    my_bot.run()