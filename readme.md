create venv:
    python -m venv venv
activate venv:
    .\venv\Scripts\Activate.ps1    
    or .venv\Scripts\activate.bat


libraries:
    pip install "fastapi[all]"
    pip install aiogram
    python -m pip install "pymongo[srv]"
-----------------------------------------
init requirements.txt
    pip freeze > requirements.txt    

start fastapi:
    1) fastapi dev main.py
    2) uvicorn main:app --reload
    3) python main.py (__main__)  

telegram lessons:
    https://habr.com/ru/articles/953902/
    https://habr.com/ru/articles/955062/
    https://habr.com/ru/articles/955986/

telegram api:
    https://docs.python-telegram-bot.org/en/v12.5.1/index.html    


-------
https://tonyline.com.ua/ru/tools/emoji/#txt10h2    


mongodb+srv://test:<db_password>@cluster0.cdoc0v3.mongodb.net/?appName=Cluster0
zaqWSX    
-----------------------
🚗 Главное меню
Записаться на сервис: Основная кнопка для перехода к выбору услуги и времени.
Услуги и цены: Список доступных работ (ТО, диагностика, ходовая, двигатель и т.д.) с актуальными прайсами.
Мои записи: Просмотр текущих бронирований с возможностью отмены или переноса.
Акции и новости: Специальные предложения для клиентов (например, «Подготовка к зиме» или скидка на первую замену масла).
О нас и контакты: Адрес (с ссылкой на карту), режим работы, номер телефона и мессенджеры для прямой связи.
📝 Процесс записи (пошаговый)
Выбор автомобиля: Возможность выбрать из сохраненных ранее или ввести новую марку/модель и госномер.
Выбор типа работ: Выпадающий список категорий (замена масла, шиномонтаж, ремонт АКПП и т.д.).
Выбор даты и времени: Интерактивный календарь с доступными «слотами».
Описание проблемы: Поле для ввода текста или записи аудиосообщения (например, «стук в передней части при повороте»).
Контактные данные: Запрос номера телефона через кнопку Share Contact (если пользователь новый).
Подтверждение: Итоговое сообщение со всеми данными и кнопкой «Подтвердить запись».
🛠 Личный кабинет (Профиль клиента)
Гараж: Список автомобилей пользователя для быстрой записи.
История обслуживания: Протоколы прошлых визитов и рекомендации мастеров (если есть интеграция с CRM).
Бонусная карта: Баланс баллов или уровень скидки по программе лояльности.
---------------------
npm i -g vercel
vercel login
cd prj folder
 for start:   vercel --prod
 for remove:  vercel rm telepy-aru2f05rb-scurto-s-projects.vercel.app

