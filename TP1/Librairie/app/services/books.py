from app.schemas.books import Book
from app.database import bookstore


def get_all_books() -> list[Book]:
    books_data = bookstore["tasks"]
    books = [Book.model_validate(data) for data in books_data]
    return books

def spacebars_only(text: str) -> bool:
    """Check if a string contains only spaces"""
    t = text.strip()
    return (len(t)<=0)

def check_input_validity(*args):
    for input in args:
        # Check if empty string :
        if len(input) < 1:
            raise ValueError("All the fields must be filled")
        # Check if only spacebars :
        i = input.strip()
        if len(i) < 1:
            raise ValueError("Please provide real title, author and editor")
    return
    
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
    # 2 books can have the same title, author or edithor but not all at once
    bookstore["books"].append(new_book)
    return new_book


def delete_book_data(book_id):
    bookstore["books"] = [
        book for book in bookstore["books"]
        if not (book["id"] == book_id)
    ]


"""def update_book(book_id, updated_fields: dict):
    # Find the book to be updated by its id 
    target_book = get_book_by_id(book_id)
    
    # Merge the updates into the target book's fields
    for key in updated_fields.keys():
        target_book[key] = updated_fields[key]
        
    # Save the updated book back into the database
    save_book(target_book)  
    
    return target_book"""

def update_book_data(book_id, updated_fields: dict):
    # Find the book to be updated by its id
    target_book = get_book_by_id(book_id)
    
    # If the book is found, update it with the new values
    if target_book is not None:
        # Merge the updates into the target book's fields
        for key in updated_fields.keys():
            target_book[key] = updated_fields[key]
        
        # Find the index of the updated book in the 'bookstore["books"]' list
        book_index = bookstore["books"].index(target_book)
        
        # Save the updated book back into the database
        bookstore["books"][book_index] = target_book
        
        # Return the updated book object
        return Book.model_validate(target_book)
    else:
        return None