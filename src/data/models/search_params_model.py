# type: ignore
from pydantic.main import BaseModel
from src.core.enums.providers import Providers
from typing import List


class SearchParams(BaseModel):
    search: str
    providers: List[Providers]
