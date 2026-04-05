from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

data = [
    {
        "id": 1,
        "author": "author_1",
        "title": "title_1",
    },
    {
        "id": 2,
        "author": "author_2",
        "title": "title_2",
    },
    {
        "id": 3,
        "author": "author_3",
        "title": "title_3",
    },
    {
        "id": 4,
        "author": "author_4",
        "title": "title_4",
    }
]

class Book(BaseModel):
    author: str
    title: str

@router.get("/books")
def books():
    return data

@router.get("/books/{id}")
def get_book(id: int):
    for book in data:
        if book["id"] == id:
            return book
    raise HTTPException(status_code=404, detail="Not found")


@router.post("/books")
def add_book(new_book: Book):   
    data.append({
        "id": len(data) +1,
        "author": new_book.author,
        "title": new_book.title
    })
    
    return {
        "success": True
    }