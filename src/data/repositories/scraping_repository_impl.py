from typing import List, Type
from src.domain.repositories.scraping_repository import ScrapingRepository
from src.domain.entities.poster_entity import PosterEnitity
from src.domain.errors.failures import Failure
from src.data.datasources.scraping_datasource import ScrapingDatasource


class ScrapingRepositoryImpl(ScrapingRepository):
    def __init__(self, datasource: Type[ScrapingDatasource]):
        self.datasource = datasource

    def get_posters(self) -> List[PosterEnitity]:
        try:
            return self.datasource.get_posters()
        except Failure as error:
            raise error
