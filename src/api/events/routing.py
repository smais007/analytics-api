from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_event():
    return {
        "items": ["event1", "event2", "event3"]
    }