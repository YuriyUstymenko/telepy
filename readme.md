create venv:
    python -m venv venv
activate venv:
    .\venv\Scripts\Activate.ps1    


libraries:
    pip install "fastapi[all]"

start fastapi:
    1) fastapi dev main.py
    2) uvicorn main:app --reload
    3) from main.py (__main__)  