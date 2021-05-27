# type: ignore
from abc import ABC, abstractmethod
from src.domain.entities.poster_entity import PosterEnitity
from typing import List


class ScrapingRepository(ABC):
    @abstractmethod
    def get_posters(self) -> List[PosterEnitity]:
        pass  # noqa: W292
