create venv:
    python -m venv venv
activate venv:
    .\venv\Scripts\Activate.ps1    


libraries:
    pip install "fastapi[all]"
    pip install aiogram

start fastapi:
    1) fastapi dev main.py
    2) uvicorn main:app --reload
    3) python main.py (__main__)  

telegram lessons:
    https://habr.com/ru/articles/953902/
    https://habr.com/ru/articles/955062/
    https://habr.com/ru/articles/955986/