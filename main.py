from fastapi import FastAPI
from routes import permissions
from routes import books
from handlers import basic_handlers, menu_handlers
import uvicorn
import asyncio
import logging

from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters.command import Command
from aiogram.types import BotCommand, MenuButtonCommands

from pymongo import AsyncMongoClient

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

client = AsyncMongoClient("mongodb+srv://test:zaqWSX@cluster0.cdoc0v3.mongodb.net/?appName=Cluster0")
db = client["test_database"]


async def delete_webhook():
    await bot.delete_webhook(drop_pending_updates=True) 
async def start_polling():    
    try:
        await dp.start_polling(bot, db=db)
    finally:
        client.close()
async def start_uvicorn():
    config = uvicorn.Config("main:app", reload=True, port=8000, log_level="info")
    server = uvicorn.Server(config)
    await server.serve() 
    
async def set_menu_button(bot: Bot):
    # Сначала регистрируем сами команды
    await bot.set_my_commands([
        BotCommand(command="start", description="Запустить бота"),
        BotCommand(command="help", description="Помощь")
    ])
    
    # Затем устанавливаем кнопку меню на открытие этого списка
    await bot.set_chat_menu_button(
        menu_button=MenuButtonCommands()
    )    

async def mongo_db():
    # Connect to MongoDB
    client = AsyncMongoClient("mongodb+srv://test:zaqWSX@cluster0.cdoc0v3.mongodb.net/?appName=Cluster0")
    db = client["test_database"]
    collection = db["test_collection"]

    # Insert a document
    #result = await collection.insert_one({"name": "Alice", "role": "admin"})
    #print(f"Inserted ID: {result.inserted_id}")

    # Find a document
    #document = await collection.find_one({"name": "Alice"})
    #print(f"Found: {document}")

    # Iterate over multiple documents
    #async for doc in collection.find({"role": "admin"}):
        #print(doc)            

async def main():
    dp.include_router(menu_handlers.router)
    dp.include_router(basic_handlers.router)    
    results = await asyncio.gather(delete_webhook(), start_polling(), start_uvicorn(), set_menu_button(bot=bot))

if __name__ == "__main__":    
    asyncio.run(main())