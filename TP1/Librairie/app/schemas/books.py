from pydantic import BaseModel, Field


class Book(BaseModel):
    id: str = Field(min_length=4,max_length=4)
    name: str = Field(min_length=3, max_length=50)
    author: str
    editor :str
    