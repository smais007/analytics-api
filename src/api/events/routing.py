from fastapi import APIRouter
from .schema import EventSchema


from api.db.config import DATABASE_URL 


router = APIRouter()

@router.get("/")
def read_events():
    return {
        "items": ["event1", "event2", "event3"]
    }


@router.get("/{event_id}")
def read_event(event_id:int) -> EventSchema:
    return EventSchema(id= event_id)