from fastapi import FastAPI
from routes import permissions
from routes import books
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return "Hello World"


app.include_router(books.router)
app.include_router(permissions.router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)