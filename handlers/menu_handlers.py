from aiogram import Router, types
from aiogram.filters.command import Command

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я бот, и моя логика вынесена в отдельный файл.")

@router.message(Command("menu"))
async def show_menu(message: types.Message):
    # Используем HTML-разметку для формирования текста
    text = (
        "<b>Меню возможностей:</b>\n\n"
        "<i>Этот бот демонстрирует:</i>\n"
        " - Отправку форматированного текста\n"
        " - Отправку изображений и документов\n\n"
        "Воспользуйтесь командой /send_photo, чтобы получить картинку.\n\n"
        "Больше информации о фреймворке вы найдете в "
        "<a href='https://aiogram.dev/'>документации aiogram 3</a>."
    )
    
    # Отправляем сообщение, обязательно указав parse_mode
    await message.answer(text, parse_mode="HTML")