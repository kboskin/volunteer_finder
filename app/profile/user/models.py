from dataclasses import field

from pydantic.dataclasses import dataclass
from typing import List
from uuid import UUID
from datetime import datetime


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
