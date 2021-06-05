# type: ignore
from src.domain.entities.poster_entity import PosterEntity
from src.domain.entities.details_entity import DetailsEntity
from typing import List, Type
from src.domain.repositories.scraping_repository import ScrapingRepository
from src.data.models.result_search_model import ResultSearchModel
from src.domain.errors.failures import Failure
from src.data.datasources.scraping_datasource import ScrapingDatasource


class ScrapingRepositoryImpl(ScrapingRepository):
    def __init__(self, datasource: Type[ScrapingDatasource]):
        self.datasource = datasource

    def get_posters(self, content: bytes) -> List[PosterEntity]:
        try:
            return self.datasource.get_posters(content)
        except Failure as error:
            raise error

    def result_search(self, content: bytes) -> List[ResultSearchModel]:
        try:
            return self.datasource.result_search(content)
        except Failure as error:
            raise error

    def get_details(self) -> DetailsEntity:
        try:
            return self.datasource.get_details()
        except Failure as error:
            raise error
