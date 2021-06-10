# type: ignore
from abc import ABC, abstractmethod
from src.domain.entities.poster_entity import PosterEntity
from src.domain.entities.result_search_entity import ResultSearchEntity
from src.domain.entities.details_entity import DetailsEntity
from typing import List


class ScrapingRepository(ABC):
    @abstractmethod
    def get_posters(self) -> List[PosterEntity]:
        pass  # noqa: W292

    @abstractmethod
    def result_search(self) -> List[ResultSearchEntity]:
        pass  # noqa: W292

    @abstractmethod
    def get_details(self) -> DetailsEntity:
        pass  # noqa: W292
