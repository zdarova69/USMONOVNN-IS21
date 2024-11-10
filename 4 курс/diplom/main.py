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
    greeting = '''🚀 Приветствую тебя дорогой друг. 🌟

🤖 Я - чат бот, работающий с большими языковыми моделями, а именно:
✅ OpenAI ChatGPT и DALL-E
✅ Sber Gigachat и Kandinsky 3.1
✅ Google Gemini
✅ Deepseek

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
    payment_check = await payment(value='1', description='подписка на телеграмм-бота')
    payment_url = payment_check['confirmation']['confirmation_url']

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