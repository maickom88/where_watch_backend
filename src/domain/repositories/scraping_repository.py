# type: ignore
from abc import ABC, abstractmethod
from src.domain.entities.poster_entity import PosterEntity
from typing import List


class ScrapingRepository(ABC):
    @abstractmethod
    def get_posters(self, content: bytes) -> List[PosterEntity]:
        pass  # noqa: W292
