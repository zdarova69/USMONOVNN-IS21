import json
import telebot
from telebot import types
import os
from collections import Counter
import re

class MyBot:
    def __init__(self):
        self.token = "6095239590:AAGLodvJdqeE7EK-dfiFtZgsr8WtSwwd1-4"
        self.bot = telebot.TeleBot(self.token)

        self.count = 0

        self.greeting_list = r"\b(Прив|Здравст|Здар|Hello|Hi)\w*\b"
        self.farewell_list =  r"\b(Пока|Прощ|bye|Досвид)\w*\b"

        self.markup1 = types.InlineKeyboardMarkup(row_width=2)
        self.item0 = types.InlineKeyboardButton(text="имя", callback_data="имя")
        self.item1 = types.InlineKeyboardButton(text="хобби", callback_data="хобби")
        self.item2 = types.InlineKeyboardButton(text="возраст", callback_data="возраст")
        self.item3 = types.InlineKeyboardButton(text="жим лежа", callback_data="жим лежа")
        self.item4 = types.InlineKeyboardButton(text="часов в кох", callback_data="часов в кох")       
        
        self.item_work = types.InlineKeyboardButton(text="показать список", callback_data="показать список")
        self.item_add_work = types.InlineKeyboardButton(text="добавить в список", callback_data="добавить в список")

        self.kb = self.markup1.add(self.item0, self.item1, self.item2, self.item3, self.item_work, self.item_add_work)

    def run(self):
        @self.bot.message_handler(content_types=['sticker'])
        def game(message):
            self.bot.send_dice(message.chat.id)
        @self.bot.message_handler(commands=['photo'])
        def send_my_photo(message):
            photo = open('789.jpg', 'rb')
            self.bot.send_photo(message.chat.id, photo, 'это ты')
        @self.bot.message_handler(commands=['start'])
        def welcome(message):
            self.bot.reply_to(message, "Привет! Я бот кода будузего. Я могу сыграть с тобой в кости,отправь мне стикер. Могу отправлять тебе текстовые файлы", reply_markup=self.kb)
        
        # урок 17 работа с файлами
        @self.bot.message_handler(commands=['file'])
        def file(message):
            file_name = message.from_user.id
            with open(str(file_name), 'r', encoding='utf-8') as file_to_write:
                self.bot.send_document(message.chat.id, file_to_write)
        
        @self.bot.message_handler(commands=['add'])
        def add(message):
            file_name = message.from_user.id
            with open( 'add_' + str(file_name), 'w', encoding='utf-8') as file_to_write:
                file_to_write.write(message.text[5:] + '\n')
        
        @self.bot.message_handler(commands=['show'])
        def show(message):
            file_name = message.from_user.id
            with open('add_' + str(file_name), 'r', encoding='utf-8') as file_to_write:
                text_ = file_to_write.read()
                print(text_, type(text_))
                self.bot.reply_to(message, text=text_)
        
        @self.bot.message_handler(commands=['json'])
        def add_to_json(message):
            file_name = message.from_user.id
            mes_text = message.text[6:]
            lesson, description , deadline =  mes_text.split(',')

            data = {self.count:{'занятие': lesson,
                                'описание': description,
                                'дедлайн': deadline}
            }
            self.count+=1
            self.bot.reply_to(message, f'сохранено {self.count}')
            with open(str(file_name) + '.json', 'a', encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
                
        @self.bot.message_handler(content_types=['text'])
        def regex_answer(message):
            matches = re.findall(self.greeting_list, message.text, flags=re.IGNORECASE)
            if len(matches) >= 1:
                self.bot.reply_to(message, 'Привет')
            
            matches = re.findall(self.farewell_list, message.text, flags=re.IGNORECASE)
            if len(matches) >= 1:
                self.bot.reply_to(message, 'Пока')
        
        
        
        #работа с json
        @self.bot.message_handler(content_types=['document']) 
        def download_json(message):
            file_info = self.bot.get_file(message.document.file_id)
            downloaded_file = self.bot.download_file(file_info.file_path)
            new_file_path = "data_2.json"
            
            self.bot.reply_to(message, "отправь мне название ключа")
            
            with open(new_file_path, 'wb') as new_file:
                    new_file.write(downloaded_file)
           

            @self.bot.message_handler(content_types = ['text'])
            def rewrite_name_file(message):
                
                text = message.text
                with open(new_file_path, 'r', encoding="utf-8") as json_file:
                    json_dict = json.load(json_file)
                
                strings = []
                for key,item in json_dict[text].items():
                    strings.append("{}: {}".format(key.capitalize(), item))
                
                result = "; ".join(strings)
                self.bot.reply_to(message, result)
        #работа с json
        @self.bot.callback_query_handler(func=lambda call: True)
        def callback_inline(call):
            with open('задание 1\data.json', 'r', encoding="utf-8") as json_file:
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
            elif call.data == 'показать список':
                print(call.message.chat.id)
                with open(str(call.message.chat.id) + '.json', 'r', encoding='utf-8') as file_to_write:
                    self.bot.send_document(call.message.chat.id, file_to_write)
            elif call.data == 'добавить в список':
                self.bot.send_message(call.message.chat.id, 'отправь мне данные в формате: /json дело, описание, дедлайн. Например: \n /json читать, читать книгу, 21:00 ')

   
        self.bot.polling(none_stop=True)

if __name__ == '__main__':
    my_bot = MyBot()
    my_bot.run()
