import asyncio
import logging
import sys
from datetime import datetime

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.filters import Command

from datetime import datetime
# from gen_message import generate_messange
from client import Client
from payments import payment
# Открываем файл в режиме чтения
with open('tg_api.txt', 'r') as file:
    # Читаем содержимое файла
    TOKEN = file.read()

# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()
cl = Client()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    greeting = greeting = '''🚀 Приветствую тебя дорогой друг. 🌟

🤖 Я - чат бот, работающий с большими языковыми моделями, а именно:

✅ **OpenAI ChatGPT и DALL-E**
   - **ChatGPT**: Это мощная языковая модель, способная генерировать человекоподобный текст на основе входных данных. Она может отвечать на вопросы, вести диалог, создавать истории и многое другое.
   - **DALL-E**: Это модель, способная создавать изображения на основе текстовых описаний. Она может генерировать уникальные и креативные изображения, соответствующие заданным описаниям.
   - **OpenAI O1**: Это оптимизированная модель для обработки естественного языка, разработанная OpenAI. Она предназначена для высокопроизводительных задач, таких как анализ текста, классификация и извлечение информации. OpenAI O1 обеспечивает быструю и эффективную обработку данных, что делает её идеальной для приложений, требующих высокой скорости и точности.

✅ **Sber Gigachat и Kandinsky 3.1**
   - **Gigachat**: Это российская языковая модель, разработанная Сбербанком. Она обладает высокой способностью к пониманию и генерации текста на русском языке.
   - **Kandinsky 3.1**: Это модель для генерации изображений, названная в честь русского художника Казимира Малевича. Она способна создавать абстрактные и художественные изображения на основе текстовых описаний.

✅ **Google Gemini**
   - **Gemini**: Это многофункциональная модель искусственного интеллекта от Google, которая объединяет в себе возможности обработки естественного языка, генерации изображений и других задач. Она способна выполнять широкий спектр задач, от диалога до анализа данных.

✅ **Deepseek**
   - **Deepseek**: Это модель, специализирующаяся на глубоком поиске и анализе информации. Она способна извлекать ценные данные из больших объемов текста, помогая в исследованиях и анализе данных.

🔍 Чем могу помочь? Вот несколько вещей, которые ты можешь узнать или сделать прямо сейчас:

/start - Начать общение с ботом
/help - Получить помощь и список доступных команд
/buy - оформить подписку и поддержать работу бота
/gen_image - сгенерировать картинку
/choose_model - выбор модели

Удачи и успеха в твоих начинаниях! 💻🎉'''
    await message.answer(greeting)
    
    
    cl.new_user(tgID=message.from_user.id, name=message.from_user.full_name, date_start=datetime.now())
# Обработчики команд
@dp.message(Command("buy"))
async def cmd_buy(message: Message):
    payment_url = cl.create_payment(tgID=message.from_user.id, value='1', description='Подписка на телеграмм-бота')
    if payment_url == 'у вас есть подписка':
        await message.answer(f'✅ У вас уже оформлена подписка', reply_markup=keyboard)
    else:
        buttons = [[InlineKeyboardButton(text="Оплатить подписку", url=payment_url)],
                [InlineKeyboardButton(text="Подтвердить оплату", callback_data="confirm_subscription")]
        ]
        keyboard = InlineKeyboardMarkup(inline_keyboard=buttons, row_width=2)
        # Отправляем сообщение с кнопкой
        await message.answer(f'Совершите оплату подписки 1 руб.', reply_markup=keyboard)

# # Обработчик callback запросов
@dp.callback_query(lambda c: c.data == 'confirm_subscription')
async def process_callback_get_image(callback: CallbackQuery):
     await callback.answer(f"оплата подтверждена")

@dp.message(Command("choose_model"))
async def choose_model(message: Message):
    buttons = [[InlineKeyboardButton(text="Sber GigaChat", callback_data="Sber GigaChat")],
        [InlineKeyboardButton(text="OpenAI GPT-4.0", callback_data="OpenAI GPT-4.0")],
        [InlineKeyboardButton(text="OpenAI o1", callback_data="OpenAI o1")],
        [InlineKeyboardButton(text="Google Gemini", callback_data="Google Gemini")],
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons, row_width=2)
    await message.answer('Выберите модель', reply_markup=keyboard)

@dp.callback_query(lambda c: c.data in ["Sber GigaChat", "OpenAI GPT-4.0", "OpenAI o1", "Google Gemini", "Deepseek"])
async def process_callback(callback_query: CallbackQuery):
    tgID = callback_query.from_user.id
    model = callback_query.data

    await callback_query.answer(f'Выбрана модель: {model}')
    await callback_query.message.edit_text(f'Выбрана модель: {model}', reply_markup=None)

    cl = Client()
    cl.change_model(tgID=tgID, model=model)

@dp.message(Command("help"))
async def cmd_help(message: Message):
    help_message = '''
/buy - оформить подписку и поддержать работу бота
/gen_image - сгенерировать картинку
/choose_model - выбор модели
техподдержка - @zdarova_69
        '''
    await message.reply(help_message)


@dp.message()
async def message_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received message
        print(message.text)
        answer = cl.generate_text(tgID=message.from_user.id ,prompt=message.text)
        await message.reply(answer)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())