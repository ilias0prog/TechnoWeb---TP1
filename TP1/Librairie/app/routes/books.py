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
    new_book_data = {
        "id": str(uuid4()),
        "name" : name,
        "author" : author,
        "editor" : editor
    }
    try:
        new_book = Book.model_validate(new_book_data)
    except ValidationError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid name or description for the task.",
        )
    service.save_book(new_book)
    return JSONResponse(new_book.model_dump())
# made by copilot
@router.get('/{book_id}')
def delete_book(book_id : str):
    book = service.get_book_by_id(book_id)
    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found",
        )
    service.delete_book(book)
    return JSONResponse(
        content=book.model_dump(),
        status_code=200,)

@router.post('/')
#made by copilot
def update_book(name : str, author : str, editor : str):
    new_book_data = {
        "id": str(uuid4()),
        "name" : name,
        "author" : author,
        "editor" : editor
    }
    try:
        new_book = Book.model_validate(new_book_data)
    except ValidationError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid name or description for the task.",
        )
    service.save_book(new_book)
    return JSONResponse(new_book.model_dump())
    