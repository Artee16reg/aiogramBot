from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Text
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)
from config import TOKEN
from aiogram.utils.keyboard import ReplyKeyboardBuilder
bot: Bot = Bot(token=TOKEN)
dp: Dispatcher = Dispatcher()

kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
buttons: list[KeyboardButton] = [KeyboardButton(
                text=f'Кнопка {i + 1}') for i in range(8)]
kb_builder.row(*buttons, width=4)
# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Вот такая получается клавиатура',
                         reply_markup=kb_builder.as_markup(
                             resize_keyboard=True))


#
# # Создаем объекты кнопок
# button_1: KeyboardButton = KeyboardButton(text='Собак 🦮')
# button_2: KeyboardButton = KeyboardButton(text='Огурцов 🥒')
#
# # Создаем объект клавиатуры, добавляя в него кнопки
# keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
#     keyboard=[[button_1, button_2]], resize_keyboard=True, )
#
#
# # Этот хэндлер будет срабатывать на команду "/start"
# # и отправлять в чат клавиатуру
# @dp.message(CommandStart())
# async def process_start_command(message: Message):
#     await message.answer(text='Чего кошки боятся больше?',
#                          reply_markup=keyboard)  # можно добавить one_time_keyboard=True для скрытия
#
#
# # Этот хэндлер будет срабатывать на ответ "Собак 🦮" и удалять клавиатуру
# @dp.message(Text(text='Собак 🦮'))
# async def process_dog_answer(message: Message):
#     await message.answer(text='Да, несомненно, кошки боятся собак. '
#                               'Но вы видели как они боятся огурцов?',
#                          reply_markup=ReplyKeyboardRemove())


# Этот хэндлер будет срабатывать на ответ "Огурцов 🥒" и удалять клавиатуру
@dp.message(Text(text='Огурцов 🥒'))
async def process_cucumber_answer(message: Message):
    await message.answer(text='Да, иногда кажется, что огурцов '
                              'кошки боятся больше',
                         reply_markup=ReplyKeyboardRemove())  # можно не удалять, а скрывать после нажатия


if __name__ == '__main__':
    dp.run_polling(bot)
