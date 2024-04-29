import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

import sqlite3

vk_session = vk_api.VkApi(token="vk1.a.9CPPgQzIdvuFDqNRpQHEdkbxdRSRXcv5eVDO_FihpQlDMSBXMfedm9_akMbU6KEaEWXs7BhAPxWsu9NZ5kD_qrEMHr_1Mg7pgwXRi7uh-JxpSCB36T3xh10OmJB5iBUcUFniE1jSFHG0J6rC2UHi0Rr4u4ecKSRyCbvvkj21AdMHW-tat6HjPQrvWOzkVbV28azMfur6AL2nnMdV4mJMCQ")
vk = vk_session.get_api()
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)


# Подключение к базе данных SQLite
conn = sqlite3.connect('database.db', check_same_thread=False)
cursor = conn.cursor()

# Создание таблиц в базе данных
cursor.execute('''CREATE TABLE IF NOT EXISTS greetings (
                    id INTEGER PRIMARY KEY,
                    message TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS farewells (
                    id INTEGER PRIMARY KEY,
                    message TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS topics (
                    id INTEGER PRIMARY KEY,
                    keyword TEXT,
                    content TEXT)''')

# Функция для отправки сообщения
def send_message(user_id, message):
    vk.messages.send(user_id=user_id, message=message, random_id=0)

# Обработчик команды /start
def start(user_id):
    send_message(user_id, "Приветствую!")

# Обработчик команды /end
def end(user_id):
    send_message(user_id, "До свидания!")

# Обработчик команды /add_greeting
def add_greeting(user_id, message):
    cursor.execute("INSERT INTO greetings (message) VALUES (?)", (message,))
    conn.commit()
    send_message(user_id, f"Сообщение для приветствия успешно добавлено: {message}")

# Обработчик команды /add_farewell
def add_farewell(user_id, message):
    cursor.execute("INSERT INTO farewells (message) VALUES (?)", (message,))
    conn.commit()
    send_message(user_id, f"Сообщение для прощания успешно добавлено: {message}")

# Обработчик команды /add_topic
def add_topic(user_id, keyword, content):
    cursor.execute("INSERT INTO topics (keyword, content) VALUES (?, ?)", (keyword, content))
    conn.commit()
    send_message(user_id, f"Контент для ключевого слова '{keyword}' успешно добавлен")

# Обработчик команды /menu
def menu(user_id):
    menu_text = "Меню:\n"
    menu_text += "/start - приветствие\n"
    menu_text += "/end - прощание\n"
    menu_text += "/add_greeting <сообщение> - добавить сообщение для приветствия\n"
    menu_text += "/add_farewell <сообщение> - добавить сообщение для прощания\n"
    menu_text += "/add_topic <ключевое слово> <контент> - добавить контент для ключевого слова"
    send_message(user_id, menu_text)

# Обработчик входящих сообщений
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        user_id = event.user_id
        message = event.text.lower()
        
        if message == "/start":
            start(user_id)
        elif message == "/end":
            end(user_id)
        elif message.startswith("/add_greeting"):
            _, greeting_message = message.split(maxsplit=1)
            add_greeting(user_id, greeting_message)
        elif message.startswith("/add_farewell"):
            _, farewell_message = message.split(maxsplit=1)
            add_farewell(user_id, farewell_message)
        elif message.startswith("/add_topic"):
            _, keyword, content = message.split(maxsplit=2)
            add_topic(user_id, keyword, content)
        elif message == "/menu":
            menu(user_id)
