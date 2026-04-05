from fastapi import APIRouter

router = APIRouter()

@router.get("/books")
def books():
    return "all books"