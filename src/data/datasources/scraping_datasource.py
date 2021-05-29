from abc import ABC, abstractmethod
from typing import List
from src.data.models.poster_model import PosterModel


class ScrapingDatasource(ABC):
    @abstractmethod
    def get_posters(self) -> List[PosterModel]:
        pass
