from datetime import datetime
from typing import List

from pydantic import BaseModel


class ItemBase(BaseModel):
    size: float
    directory: str
    file_name: str
    type: str
    locations: List[str]
    mimetype: str | None
    version: str | None
    created_by: datetime
    modified_by: datetime
    created_date: datetime
    modified_date: datetime


# For creating Items
class ItemCreate(ItemBase):
    pass


# For reading Items
class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True


class VersionBase(BaseModel):
    number: int
    dependencies: List[ItemBase] = []


class VersionCreate(BaseModel):
    pass


class Version(VersionBase):
    id: int

    class Config:
        orm_mode = True