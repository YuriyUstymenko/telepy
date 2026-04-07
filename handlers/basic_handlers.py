from aiogram import Router, types, F
from aiogram.filters.command import Command

# Все роутеры нужно именовать так, чтобы не было конфликтов
router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я бот, и моя логика вынесена в отдельный файл.")


# Хэндлер на получение фото
@router.message(F.photo)
async def handle_photo(message: types.Message):
    await message.answer("Отличное фото! Спасибо.")


# Хэндлер на получение стикера
@router.message(F.sticker)
async def handle_sticker(message: types.Message):
    # message.sticker.file_id - можно получить id стикера
    await message.answer("Милый стикер!")


# Хэндлер на любой текст (самый общий, должен быть последним)
@router.message(F.text)
async def handle_text(message: types.Message):
    await message.answer(f"Ты прислал текст: {message.text}")    

@router.message()
async def echo_message(message: types.Message):
    await message.answer(f"Я получил твое сообщение: {message.text}")