from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime


class Review(BaseModel):
    id: int = Field(alias='review_id')
    text:str
    date:datetime
    author_id:str
    author_name:str
    likes:Optional[int]
