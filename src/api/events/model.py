from typing import List, Optional
from sqlmodel import SQLModel, Field


class EventModel(SQLModel):
    # id: Optional[int] = Field(default=None, primary_key=True)
    id: int
    page: Optional[str] = ""
    description: Optional[str] =""


class EventCreateModel(SQLModel):
    page: str
    description: Optional[str] = Field(default="")



class EventUpdateModel(SQLModel):
    description: str



class EventListModel(SQLModel):
    results: List[EventModel]
    count: int