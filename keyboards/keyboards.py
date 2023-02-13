from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from lexicon.lexicon_ru import LEXICON_RU

# Создаем клавиатуру с кнопками "Давай!" и "Не хочу!"
yes_no_kb: ReplyKeyboardBuilder = ReplyKeyboardBuilder()  # one_time_keyboard=True,
# resize_keyboard=True
# Создаем объекты кнопок
button_yes: KeyboardButton = KeyboardButton(text=LEXICON_RU['yes_button'])
button_no: KeyboardButton = KeyboardButton(text=LEXICON_RU['no_button'])

# Располагаем кнопки в клавиатуре рядом друг с другом в одном ряду
yes_no_kb.row(button_yes, button_no)

# Создаем игровую клавиатуру с кнопками "Камень 🗿", "Ножницы ✂" и "Бумага 📜"
game_kb: ReplyKeyboardBuilder = ReplyKeyboardBuilder()  # resize_keyboard=True

button_1: KeyboardButton = KeyboardButton(text=LEXICON_RU['rock'])
button_2: KeyboardButton = KeyboardButton(text=LEXICON_RU['scissors'])
button_3: KeyboardButton = KeyboardButton(text=LEXICON_RU['paper'])

# Располагаем кнопки в клавиатуре одну под другой в 3 ряда
game_kb.add(button_1).add(button_2).add(button_3)
