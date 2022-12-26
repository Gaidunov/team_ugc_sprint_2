from pydantic import BaseModel, Field
from datetime import datetime
from uuid import UUID


class Review(BaseModel):
    id: int = Field(alias="review_id")
    text: str
    date: datetime
    author_id: str
    author_name: str
