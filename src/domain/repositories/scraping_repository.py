# type: ignore
from abc import ABC, abstractmethod
from src.domain.entities.poster_entity import PosterEntity
from src.domain.entities.result_search_entity import ResultSearchEntity
from typing import List


class ScrapingRepository(ABC):
    @abstractmethod
    def get_posters(self, content: bytes) -> List[PosterEntity]:
        pass  # noqa: W292

    @abstractmethod
    def result_search(self, content: bytes) -> List[ResultSearchEntity]:
        pass  # noqa: W292
