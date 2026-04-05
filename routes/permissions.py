from fastapi import APIRouter

router = APIRouter()

@router.get("/books2")
def books():
    return "all books2"