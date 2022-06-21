from pydantic.class_validators import Union
from pydantic.dataclasses import dataclass


@dataclass
class Category:
    id: int
    parent_id: Union[int, None] = None
    category_name: str
