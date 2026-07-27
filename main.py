from uuid import uuid4

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
)


class TaskSchema(BaseModel):
    id: str
    title: str
    completed: bool



class TaskCreateSchema(BaseModel):
    title: str

class BookSchema(BaseModel):
    book: str


tasks: list[TaskSchema] = []
book = ''
def read_base_page():
    return {"message": "Hello World"}


@app.get("/tasks")
def read_tasks() -> str:
    return f'Любимая книга: {book}'

@app.post("/tasks")
def create_task(payload: TaskCreateSchema) -> TaskSchema:
    print(payload)
    new_task = TaskSchema(id=str(uuid4()), title=payload.title, completed=False)
    tasks.append(new_task)
    return new_task

@app.post("/books")
def create_book(payload: BookSchema) -> BookSchema:
    global book
    book = payload.book
    return BookSchema(book=book)

