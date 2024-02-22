from app.schemas import Task
from app.database import database


def save_task(new_task: Task) -> Task:
    database["tasks"].append(new_task)
    return new_task


def get_all_books() -> list[Task]:
    tasks_data = database["tasks"]
    tasks = [Task.model_validate(data) for data in tasks_data]
    return tasks


def get_task_by_id(task_id: str) -> Task | None:
    selected_task = [
        task for task in database["tasks"]
        if task["id"] == task_id
    ]
    if len(selected_task) < 1:
        return None
    selected_task = Task.model_validate(selected_task[0])
    return selected_task
    
