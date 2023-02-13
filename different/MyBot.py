from aiogram import Bot, Dispatcher
from aiogram.filters import Command, Text
from aiogram.types import Message
from aiogram.types import ContentType
from aiogram import F
from FiltersBot import NumbersInMessage
from config_data.config import load_config

# Создаем диспетчера
dp: Dispatcher = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


# Этот хэндлер будет срабатывать на команду "/help"
async def process_help_command(message: Message):
    await message.answer('Напиши мне что-нибудь и в ответ '
                         'я пришлю тебе твое сообщение')


# Этот хэндлер будет срабатывать на отправку стикеров
async def send_sticker_echo(message: Message):
    print(message.sticker.json())
    await message.answer_sticker(message.sticker.file_id)


# Этот хэндлер будет срабатывать на отправку боту голосового сообщения
async def send_voice_echo(message: Message):
    await message.answer_voice(message.voice.file_id)


# Этот хэндлер будет срабатывать на отправку аудио файлов
async def send_audio_echo(message: Message):
    await message.answer_audio(message.audio.file_id)


# Этот хэндлер будет срабатывать на отправку видео сообщений don't work
async def send_video_note_echo(message: Message):
    await message.answer_video_note(message.video_note.file_id)


# Этот хэндлер будет срабатывать на отправку боту фото
async def send_photo_echo(message: Message):
    await message.reply_photo(message.photo[0].file_id)


# Этот хэндлер будет срабатывать на отправку видео
async def send_video_echo(message: Message):
    await message.answer_video(message.video.file_id)


# Этот хэндлер будет срабатывать на отправку любых файлов
async def send_files(message: Message):
    await message.answer_document(message.document.file_id)


# Этот хэндлер будет срабатывать, если сообщение пользователя
# начинается с фразы "найди числа" и в нем есть числа
@dp.message(Text(startswith=['найди числа', 'есть числа?'], ignore_case=True),
            NumbersInMessage())
# Помимо объекта типа Message, принимаем в хэндлер список чисел из фильтра
async def process_if_numbers(message: Message, numbers: list[int]):
    await message.answer(
        text=f'Нашел: {str(", ".join(str(num) for num in numbers))}')


# Этот хэндлер будет срабатывать, если сообщение пользователя
# начинается с фразы "найди числа", но в нем нет чисел
@dp.message(Text(startswith='найди числа', ignore_case=True))
async def process_if_not_numbers(message: Message):
    await message.answer(
        text='Не нашел что-то :(')


# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# можно отлавливать конкретные передачей в message фильтр
# полностью совпадает с каким-то текстом: Text(text='какой-то текст')
# начинается с какого-то конкретного текста: Text(startswith='начало какого-то текста')
# заканчивается каким-то текстом: Text(endswith='конец какого-то текста')
# содержит в себе какой-то текст: Text(contains='какой-то текст')
# можно добавить ignore_case=True
async def send_echo(message: Message):
    await message.reply(text=message.text)


# Этот хэндлер будет срабатывать на любые ваши сообщения,
# кроме команд "/start" и "/help"
# @dp.message()
# async def send_echo(message: Message):
#     try:
#         await message.send_copy(chat_id=message.chat.id)
#     except TypeError:
#         await message.reply(text='Данный тип апдейтов не поддерживается '
#                                  'методом send_copy')


# Регистрируем хэндлеры
dp.message.register(process_start_command, Command(commands=["start"]))
dp.message.register(process_help_command, Command(commands=['help']))
dp.message.register(send_photo_echo, F.photo)
dp.message.register(send_voice_echo, F.voice)
dp.message.register(send_audio_echo, F.audio)
dp.message.register(send_video_echo, F.video)
dp.message.register(send_sticker_echo, F.sticker)
dp.message.register(send_files, F.document)
# dp.message.register(send_video_note_echo, F.note_video) don't work
dp.message.register(send_echo)


def main() -> None:
    bot: Bot = Bot(token=load_config().tg_bot.token)
    dp.run_polling(bot)


if __name__ == '__main__':
    main()
