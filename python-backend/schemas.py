from typing import Optional
from sqlmodel import SQLModel


class ItemCreate(SQLModel):
    name: str
    is_default: bool = False
    is_enabled: bool = True


class ItemUpdate(SQLModel):
    name: Optional[str] = None
    is_enabled: Optional[bool] = None