# type: ignore
from abc import ABC, abstractmethod
from src.domain.entities.poster_entity import PosterEntity
from src.domain.entities.details_entity import DetailsEntity
from typing import List
from src.data.models.result_search_model import ResultSearchModel


class ScrapingDatasource(ABC):
    @abstractmethod
    def get_posters(self) -> List[PosterEntity]:
        pass

    @abstractmethod
    def result_search(self) -> List[ResultSearchModel]:
        pass

    @abstractmethod
    def get_details(self) -> DetailsEntity:
        pass
