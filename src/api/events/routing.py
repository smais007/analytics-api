from fastapi import APIRouter
from .model import EventModel


from api.db.config import DATABASE_URL 


router = APIRouter()

@router.get("/")
def read_events():
    return {
        "items": ["event1", "event2", "event3"]
    }


