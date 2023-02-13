from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.filters import Text, Command

from lexicon.lexicon_ru import LEXICON_RU
from keyboards.keyboards import yes_no_kb, game_kb
from services.services import get_bot_choice, get_winner


# from services.services import get_bot_choice, get_winner


# Этот хэндлер срабатывает на команду /start
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=yes_no_kb.as_markup(one_time_keyboard=True,
                                                                                     resize_keyboard=True))


# Этот хэндлер срабатывает на команду /help
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'], reply_markup=yes_no_kb.as_markup(one_time_keyboard=True,
                                                                                    resize_keyboard=True))


# Этот хэндлер срабатывает на согласие пользователя играть в игру
async def process_yes_answer(message: Message):
    await message.answer(text=LEXICON_RU['yes'], reply_markup=game_kb.as_markup(resize_keyboard=True))


# Этот хэндлер срабатывает на отказ пользователя играть в игру
async def process_no_answer(message: Message):
    await message.answer(text=LEXICON_RU['no'])


# Этот хэндлер срабатывает на любую из игровых кнопок
async def process_game_button(message: Message):
    bot_choice = get_bot_choice()
    await message.answer(text=f'{LEXICON_RU["bot_choice"]} - {LEXICON_RU[bot_choice]}')
    winner = get_winner(message.text, bot_choice)
    await message.answer(text=LEXICON_RU[winner], reply_markup=yes_no_kb.as_markup(one_time_keyboard=True,
                                                                                   resize_keyboard=True))


# Функция для регистрации хэндлеров в диспетчере. Вызывается в исполняемом файле bot.py
def register_user_handlers(dp: Dispatcher):
    dp.message.register(process_start_command, Command(commands=["start"]))
    dp.message.register(process_help_command, Command(commands=["help"]))
    dp.message.register(process_yes_answer, Text(LEXICON_RU['yes_button']))
    dp.message.register(process_no_answer, Text(LEXICON_RU['no_button']))
    dp.message.register(process_game_button, Text([LEXICON_RU['rock'], LEXICON_RU['paper'], LEXICON_RU['scissors']]))
