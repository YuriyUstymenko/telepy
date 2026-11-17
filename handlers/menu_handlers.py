from aiogram import Router, types, F
from aiogram.filters.command import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from pymongo.asynchronous.database import AsyncDatabase
import handlers.keyboards as kb

router = Router()

@router.message(Command("start"))
async def menu_start(message: types.Message, db: AsyncDatabase):
    collection = db["bot_account"]
    await message.reply("Main menu", reply_markup=await kb.inline_start_keyboard())

@router.message(Command("profile"))
async def menu_profile(message: types.Message, db: AsyncDatabase):
    #await message.reply("KeyboardButton.", reply_markup=keyboard)     
    print('Text content: ' + message.text)

    print('User id: ' + str(message.from_user.id))
    print('User username: ' + str(message.from_user.username))
    print('User full_name: ' + str(message.from_user.full_name))
    print('User first_name: ' + str(message.from_user.first_name))
    print('User last_name: ' + str(message.from_user.last_name))
    print('User is_bot: ' + str(message.from_user.is_bot))

    print('Chat id: ' + str(message.chat.id))
    print('Chat type: ' + str(message.chat.type))

    collection = db["bot_account"]
    query = {"id": message.from_user.id}
    account = await collection.find_one(query)
    print(account["username"] if account else "Not found")
    if (not account):
        new_account = {
            "id": message.from_user.id,
            "username": message.from_user.username,
            "first_name": message.from_user.first_name,
            "last_name": message.from_user.last_name,
            "is_bot": message.from_user.is_bot
        }
        account = await collection.insert_one(new_account)
        print(account)
    await message.reply(str(account))   


@router.message(Command("catalog"))
async def menu_catalog(message: types.Message, db: AsyncDatabase):
    await message.reply("KeyboardButton.", reply_markup=kb.keyboard)       

@router.message(Command("help"))
async def menu_help(message: types.Message, db: AsyncDatabase):
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
"""
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
"""
#@router.callback_query_handler(text=["btn1", "btn2"])
@router.callback_query(lambda c: c.data == 'btn1' or c.data == 'btn2')
async def handle_button_click(call: types.CallbackQuery):
    if call.data == "btn1":
        await call.message.answer("You clicked Button 1!")
    elif call.data == "btn2":
        await call.message.answer("You clicked Button 2!")
    await call.answer()

@router.callback_query(F.data == 'booking')
async def booking(callback: types.CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text("📅 Записаться на ремонт / ТО", reply_markup=await kb.inline_booking_keyboard())      

@router.callback_query(F.data == 'backToStartMenu')
async def backToStartMenu(callback: types.CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text("Main menu", reply_markup=await kb.inline_start_keyboard())     
