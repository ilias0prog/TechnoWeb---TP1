from app.schemas.books import Book
from app.database import bookstore


def get_all_books() -> list[Book]:
    books_data = bookstore["tasks"]
    books = [Book.model_validate(data) for data in books_data]
    return books


def get_book_by_id(book_id: str) -> Book | None:
    selected_book = [
        book for book in bookstore["books"]
        if book["id"] == book_id
    ]
    if len(selected_book) < 1:
        return None
    selected_book = Book.model_validate(selected_book[0])
    return selected_book

def save_book(new_book: Book) -> Book:
    bookstore["books"].append(new_book)
    return new_book

def delete_book(book_id):
    bookstore["books"] = [
        book for book in bookstore["books"]
        if not (book["id"] == book_id)
    ]

# TODO: Implement update functionality

def update_book(book_id, updated_fields: dict):
    # Find the book to be updated by its id 
    target_book = get_book_by_id(book_id)
    
    # Merge the updates into the target book's fields
    for key in updated_fields.keys():
        target_book[key] = updated_fields[key]
        
    # Save the updated book back into the database
    save_book(target_book)  
    
    return target_book
