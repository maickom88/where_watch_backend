# type: ignore
from abc import ABC, abstractmethod
from typing import List
from src.data.models.poster_model import PosterModel
from src.data.models.result_search_model import ResultSearchModel


class ScrapingDatasource(ABC):
    @abstractmethod
    def get_posters(self) -> List[PosterModel]:
        pass

    @abstractmethod
    def result_search(self) -> List[ResultSearchModel]:
        pass
