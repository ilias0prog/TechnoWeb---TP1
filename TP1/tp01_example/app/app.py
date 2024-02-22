from fastapi import FastAPI

from app.routes.tasks import router as task_router


app = FastAPI(title="My Todo List")
app.include_router(task_router)

@app.on_event('startup')
def on_startup():
    print("Server started.")


def on_shutdown():
    print("Bye bye!")
