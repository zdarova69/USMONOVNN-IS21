import telebot
import sqlite3

# Инициализация бота
bot = telebot.TeleBot('2124988062:AAFPpqVZjYT9FnKaT8rPYzyUABrLBJw6XHE')

# Подключение к базе данных SQLite
conn = sqlite3.connect('database.db')
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

# Обработчик приветствия
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет! Я бот, созданный для общения. Напиши /help, чтобы узнать мои команды.")

# Обработчик прощания
@bot.message_handler(commands=['end'])
def handle_end(message):
    bot.send_message(message.chat.id, "До свидания!")

# Обработчик команды /help
@bot.message_handler(commands=['help'])
def handle_help(message):
    instructions = "Список доступных команд:\n" \
                   "/start - приветствие\n" \
                   "/end - прощание\n" \
                   "/add_greeting <message> - добавить сообщение для приветствия\n" \
                   "/add_farewell <message> - добавить сообщение для прощания\n" \
                   "/add_topic <keyword> <content> - добавить контент для ключевого слова\n" \
                   "/menu - показать меню"
    bot.send_message(message.chat.id, instructions)

# Обработчик команды /menu
@bot.message_handler(commands=['menu'])
def handle_menu(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
    item1 = telebot.types.KeyboardButton('/add_greeting')
    item2 = telebot.types.KeyboardButton('/add_farewell')
    item3 = telebot.types.KeyboardButton('/add_topic')
    item4 = telebot.types.KeyboardButton('/help')
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, "Меню:", reply_markup=markup)

# Обработчик добавления приветствия
@bot.message_handler(commands=['add_greeting'])
def handle_add_greeting(message):
    bot.send_message(message.chat.id, "Введите сообщение для приветствия:")
    bot.register_next_step_handler(message, add_greeting)

def add_greeting(message):
    cursor.execute("INSERT INTO greetings (message) VALUES (?)", (message.text,))
    conn.commit()
    bot.send_message(message.chat.id, "Приветствие добавлено!")

# Обработчик добавления прощания
@bot.message_handler(commands=['add_farewell'])
def handle_add_farewell(message):
    bot.send_message(message.chat.id, "Введите сообщение для прощания:")
    bot.register_next_step_handler(message, add_farewell)

def add_farewell(message):
    cursor.execute("INSERT INTO farewells (message) VALUES (?)", (message.text,))
    conn.commit()
    bot.send_message(message.chat.id, "Прощание добавлено!")

# Обработчик добавления темы
@bot.message_handler(commands=['add_topic'])
def handle_add_topic(message):
    bot.send_message(message.chat.id, "Введите ключевое слово:")
    bot.register_next_step_handler(message, add_topic_keyword)

def add_topic_keyword(message):
    keyword = message.text.lower()
    bot.send_message(message.chat.id, "Введите контент для ключевого слова:")
    bot.register_next_step_handler(message, add_topic_content, keyword)

def add_topic_content(message, keyword):
    content = message.text
    cursor.execute("INSERT INTO topics (keyword, content) VALUES (?, ?)", (keyword, content))
    conn.commit()
    bot.send_message(message.chat.id, "Контент добавлен!")

# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def handle_text(message):
    # Поиск приветствия
    cursor.execute("SELECT message FROM greetings")
    greetings = cursor.fetchall()
    for greeting in greetings:
        if greeting[0].lower() in message.text.lower():
            bot.reply_to(message, "Привет!")

    # Поиск прощания
    cursor.execute("SELECT message FROM farewells")
    farewells = cursor.fetchall()
    for farewell in farewells:
        if farewell[0].lower() in message.text.lower():
            bot.reply_to(message, "До свидания!")

    # Поиск ключевых слов
    cursor.execute("SELECT keyword, content FROM topics")
    topics = cursor.fetchall()
    for topic in topics:
        if topic[0].lower() in message.text.lower():
            bot.reply_to(message, topic[1])

# Запуск бота
bot.polling()
