from fastapi import FastAPI
from routes import permissions
from routes import books
from handlers import basic_handlers, menu_handlers
import uvicorn
import asyncio
import logging

from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters.command import Command

# ВАЖНО! Вставьте сюда ваш токен, полученный от @BotFather
BOT_TOKEN = "8763588561:AAE-rRbIy63Poej57jzNEnRzYBRxdtQIRmY"

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

app = FastAPI()

@app.get("/")
def root():
    return "Hello World"

app.include_router(books.router)
app.include_router(permissions.router)




# Объект бота
bot = Bot(token=BOT_TOKEN)
# Диспетчер
dp = Dispatcher()


async def delete_webhook():
    await bot.delete_webhook(drop_pending_updates=True) 
async def start_polling():
    await dp.start_polling(bot)
async def start_uvicorn():
    config = uvicorn.Config("main:app", reload=True, port=8000, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()         

async def main():
    dp.include_router(menu_handlers.router)
    dp.include_router(basic_handlers.router)    
    results = await asyncio.gather(delete_webhook(), start_polling(), start_uvicorn())

if __name__ == "__main__":    
    asyncio.run(main())