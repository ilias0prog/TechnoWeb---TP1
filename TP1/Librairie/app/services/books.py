from app.schemas.books import Book
from app.database import database

def add_book(new_book: Book) -> Book:
    database["books"].append(new_book)
    return new_book


def get_all_books() -> list[Book]:
    books_data = database["tasks"]
    books = [Book.model_validate(data) for data in books_data]
    return books


def update_book():
    a = 0

def delete_book():





def get_task_by_id(task_id: str) -> Task | None:
    selected_task = [
        task for task in database["tasks"]
        if task["id"] == task_id
    ]
    if len(selected_task) < 1:
        return None
    selected_task = Task.model_validate(selected_task[0])
    return selected_task
    