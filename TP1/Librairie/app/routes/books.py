from uuid import uuid4

from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import ValidationError

from app.schemas.books import Book
import Librairie.app.services.books as service

router = APIRouter(prefix="/books", tags=["Books"])

@router.get('/')
def get_all_books():
    books = service.get_all_books()
    return JSONResponse(
        content=[book.model_dump() for book in books],
        status_code=200,
    )
    


@router.post('/')
def add_new_book(name : str, author : str, editor : str):
    book_data = {
        "id": str(uuid4()),
        "name" : name, 
        "author" : author,  
        "editor" : editor
    }
    try:
        new_book = Book.model_validate(book_data)
    except ValidationError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid name, author or editor.",
        )
    service.save_book(new_book)
    return JSONResponse(new_book.model_dump())



############################################
@router.post('/')
def get_book_id():
    


# Si on veut update un livre, il faut d'abord appeler get_book_id pour avoir son id et s'en servir pour l'update
@router.post('/')
def update_book(name: str, author : str, editor :str):
    