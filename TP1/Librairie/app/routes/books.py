from uuid import uuid4

from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import ValidationError

from app.schemas import books
import Librairie.app.services.books as service

router = APIRouter(prefix="/books", tags=["Books"])

@router.get('/')
def get_all_books():
    books = service.get_all_books()
    return JSONResponse(
        content=[book.model_dump() for book in books],
        status_code=200,
    )
    
