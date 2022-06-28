from dataclasses import field, dataclass

from typing import List
from datetime import datetime
from pydantic.json import UUID


@dataclass
class Feedback:
    id_from: UUID
    id_to: UUID
    rating: int
    date: datetime


@dataclass
class User:
    user_id: UUID
    first_name: str
    last_name: str
    phone_number: str
    email: str
    average_rating: int
    categories: List[str] = field(default_factory=list)
    # feedback list
    feedback: List[Feedback] = field(default_factory=list)
    # achievements
    superpowers: List[str] = field(default_factory=list)


@dataclass
class DbUser:
    user_id: UUID
    first_name: str
    last_name: str
    phone_number: str
    email: str
    is_active: bool
    deleted: bool
    created_time: datetime
    deleted_time: datetime
    updated_time: datetime

    class Config:
        orm_mode = True
