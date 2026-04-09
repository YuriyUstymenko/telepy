from aiogram import Router, types
from aiogram.filters.command import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from pymongo.asynchronous.database import AsyncDatabase

router = Router()

keyboard_inline = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Button 1", callback_data="btn1"),
        InlineKeyboardButton(text="Button 2", callback_data="btn2")
    ]
])

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Button 1"), KeyboardButton(text="Button 2")
        ],
        [
            KeyboardButton(text="Back")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.reply("Привет! Я бот, и моя логика вынесена в отдельный файл.", reply_markup=keyboard_inline)

@router.message(Command("help"))
async def cmd_start(message: types.Message):
    await message.reply("KeyboardButton.", reply_markup=keyboard)    

@router.message(Command("menu"))
async def show_menu(message: types.Message, db: AsyncDatabase):
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

    collection = db["test_collection"]
    document = await collection.find_one({"name": "Alice"})
    print(f"Found: {document}")
    text += "\n" + str(document)
    # Отправляем сообщение, обязательно указав parse_mode
    await message.answer(text, parse_mode="HTML")

#@router.callback_query_handler(text=["btn1", "btn2"])
@router.callback_query(lambda c: c.data == 'btn1' or c.data == 'btn2')
async def handle_button_click(call: types.CallbackQuery):
    if call.data == "btn1":
        await call.message.answer("You clicked Button 1!")
    elif call.data == "btn2":
        await call.message.answer("You clicked Button 2!")
    await call.answer()     