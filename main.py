from config import tg_bot_token
from aiogram import Bot, types  # на какие команды бот будет отвечат
from aiogram.dispatcher import Dispatcher  # Позволяет отслеживать обновления
from aiogram.utils import executor  # запускает бота и выолняет функции
import random


bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)


# обработчик сообщений, декоратор
@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    name = message.from_user.first_name
    full_name = message.from_user.full_name
    await message.answer(f'"<b> Привет, {name} {full_name}! </b>" \n Доступные команды /help, /info, /create', parse_mode='html')


@dp.message_handler(commands="info")
async def info_command(message: types.Message):
    await message.answer('Бот генерирует пароль')


@dp.message_handler(commands=["help"])
async def help_command(message: types.Message):
    await message.answer('Вводите размер пароля, результатом будет пароль от пароль из случайных символов и букв')


@dp.message_handler(commands=["create"])
async def create_command(message: types.Message):
    await message.answer('Введите длину пароля от 1 до 23')

lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""


# функция генерации пароля
@dp.message_handler(content_types=['text'])
async def get_password(message: types.Message):
    passlength = message.text
    try:
        passlength = int(passlength)
        if 0 < passlength <= 25:
            result = lowercase + uppercase + digits + punctuation
            password = ''.join(random.sample(result, passlength))
            await message.answer(f'Ваш пароль: \n {password}')
        else:
            await message.reply('Недопустимый размер пароля')

    except Exception as ex2:
        print(ex2)
        await message.answer('Необходимо ввести число от 1 до 23')

# запуск бота

if __name__ == '__main__':
    executor.start_polling(dp)