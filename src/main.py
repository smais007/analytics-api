from typing import Union
from contextlib import asynccontextmanager
from fastapi import FastAPI
from api.events import router as events_router
from api.db.session import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize resources here
    init_db()
    yield
    # Clean up resources here

app = FastAPI(lifespan=lifespan)
app.include_router(events_router, prefix="/api/events")

# @app.on_event("startup")
# def on_startup():
#     print("Initializing for Database")

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/healthz")
def read_api_health():
    return {"Status": "ok"}
