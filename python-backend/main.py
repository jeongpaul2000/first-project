from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, select

from db import create_db_and_tables, get_session
from models import Item
from schemas import ItemCreate, ItemUpdate

app = FastAPI()

# Middle point between frontend and backend connections
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

DEFAULT_ITEMS = [
    {"name": "apple", "is_default": True, "is_enabled": True},
    {"name": "banana", "is_default": True, "is_enabled": True},
    {"name": "grape", "is_default": True, "is_enabled": True},
]

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

    # seed defaults once
    with next(get_session()) as session:
        existing = session.exec(select(Item)).all()
        if not existing:
            for item_data in DEFAULT_ITEMS:
                session.add(Item(**item_data))
            session.commit()


@app.get("/items")
def get_items(session: Session = Depends(get_session)):
    items = session.exec(select(Item)).all()
    return items


@app.get("/items/search")
def search_items(q: str = "", session: Session = Depends(get_session)):
    items = session.exec(select(Item)).all()
    q_lower = q.lower()
    return [item for item in items if q_lower in item.name.lower()]


@app.post("/items")
def create_item(item: ItemCreate, session: Session = Depends(get_session)):
    db_item = Item(**item.model_dump())
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item


@app.put("/items/{item_id}")
def update_item(item_id: int, item: ItemUpdate, session: Session = Depends(get_session)):
    db_item = session.get(Item, item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")

    updates = item.model_dump(exclude_unset=True)
    for key, value in updates.items():
        setattr(db_item, key, value)

    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item


@app.delete("/items/{item_id}")
def delete_item(item_id: int, session: Session = Depends(get_session)):
    db_item = session.get(Item, item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")

    session.delete(db_item)
    session.commit()
    return {"ok": True}