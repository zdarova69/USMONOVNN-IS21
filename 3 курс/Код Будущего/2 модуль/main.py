import json
import telebot
from telebot import types
import os
from collections import Counter


class MyBot:
    def __init__(self):
        self.token = "6095239590:AAGLodvJdqeE7EK-dfiFtZgsr8WtSwwd1-4"
        self.bot = telebot.TeleBot(self.token)

        self.markup1 = types.InlineKeyboardMarkup(row_width=2)
        self.item0 = types.InlineKeyboardButton(text="имя", callback_data="имя")
        self.item1 = types.InlineKeyboardButton(text="хобби", callback_data="хобби")
        self.item2 = types.InlineKeyboardButton(text="возраст", callback_data="возраст")
        self.item3 = types.InlineKeyboardButton(text="жим лежа", callback_data="жим лежа")
        self.item4 = types.InlineKeyboardButton(text="в отношениях", callback_data="в отношениях")

        self.kb = self.markup1.add(self.item0, self.item1, self.item2, self.item3)
    def run(self):
        @self.bot.message_handler(commands=['start'])
        def welcome(message):
            self.bot.reply_to(message, "Привет! Я бот кода будузего", reply_markup=self.kb)
        
        @self.bot.callback_query_handler(func=lambda call: True)
        def callback_inline(call):
            with open('data.json', 'r', encoding="utf-8") as json_file:
                json_dict = json.load(json_file)  

            mas = []
            mas_i = []
            if call.data == "имя":
                for i, l in json_dict.items():
                    mas_i.append(i)
                    mas.append(l['хобби']) 
                self.bot.send_message(call.message.chat.id, f"моих друзей зовут {mas_i}")

            elif call.data == "хобби":          
                for i, l in json_dict.items():
                    mas_i.append(i)
                    mas.append(l['хобби']) 
                popular_hobbi = sum(mas, [])
                self.bot.send_message(call.message.chat.id, f"самое популярное хобби у моих друзей это {Counter(popular_hobbi).most_common(3)}")

            elif call.data == "возраст":
                for i, l in json_dict.items():
                    mas_i.append(i)
                    mas.append(l['возраст']) 
                self.bot.send_message(call.message.chat.id, f"средний возраст моих друзей {sum(mas) // len(mas)}")

            elif call.data == "жим лежа":
                for i, l in json_dict.items():
                    mas_i.append(i)
                    mas.append(l['жим лежа']) 
                self.bot.send_message(call.message.chat.id, f"средний жим лежа моих друзей {sum(mas) // len(mas)}")
            elif call.data == "кох":
                for i, l in json_dict.items():
                    mas_i.append(i)
                    mas.append(l['жим лежа']) 
                self.bot.send_message(call.message.chat.id, f"в среднем у моих друзей часов в Company of Heroes 2 {(sum(mas) // len(mas))}")
   
        self.bot.polling(none_stop=True)

if __name__ == '__main__':
    my_bot = MyBot()
    my_bot.run()
