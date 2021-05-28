from abc import ABC, abstractmethod
from typing import List
from src.domain.entities.poster_entity import PosterEnitity


class ScrapingDatasource(ABC):
    @abstractmethod
    def get_posters(self) -> List[PosterEnitity]:
        pass
