from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

keyboard_inline = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Button 1", callback_data="btn1"),
        InlineKeyboardButton(text="Button 2", callback_data="btn2")
    ]
])

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Share Contact", request_contact=True), KeyboardButton(text="Button 2")
        ],
        [
            KeyboardButton(text="Back")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

startButtons = [
    {'text': "📅 Записаться на ремонт / ТО", 'callback_data':'booking'},
    {'text': "💰 Узнать стоимость (Прайс-лист)", 'callback_data':'price'},
    {'text': "📍 Контакты и Схема проезда", 'callback_data':'contacts'},
    {'text': "🚘 Мои записи / Личный кабинет", 'callback_data':'profile'},
    {'text': "🎁 Акции и Скидки", 'callback_data':'promotion'},
    {'text': "👨‍🔧 Задать вопрос мастеру", 'callback_data':'help'}
]

async def inline_start_keyboard():
    keyboard = InlineKeyboardBuilder()
    for btn in startButtons:
        keyboard.add(InlineKeyboardButton(text=btn['text'], callback_data=btn['callback_data']))
    return keyboard.adjust(1).as_markup()


bookingButtons = [
    {'text': "🛢️ Замена масла и фильтров", 'callback_data':'1'},
    {'text': "⚙️ Диагностика подвески / ДВС", 'callback_data':'2'},
    {'text': "🛑 Тормозная система", 'callback_data':'3'},
    {'text': "❄️ Обслуживание кондиционера", 'callback_data':'4'},
    {'text': "🔧 Другой ремонт", 'callback_data':'5'},
    {'text': "🔙 Назад", 'callback_data':'backToStartMenu'}
]

async def inline_booking_keyboard():
    keyboard = InlineKeyboardBuilder()
    for btn in bookingButtons:
        keyboard.add(InlineKeyboardButton(text=btn['text'], callback_data=btn['callback_data']))
    return keyboard.adjust(1).as_markup()