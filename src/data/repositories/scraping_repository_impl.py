# type: ignore
from typing import List, Type
from src.domain.repositories.scraping_repository import ScrapingRepository
from src.data.models.poster_model import PosterModel
from src.data.models.result_search_model import ResultSearchModel
from src.domain.errors.failures import Failure
from src.data.datasources.scraping_datasource import ScrapingDatasource


class ScrapingRepositoryImpl(ScrapingRepository):
    def __init__(self, datasource: Type[ScrapingDatasource]):
        self.datasource = datasource

    def get_posters(self, content: bytes) -> List[PosterModel]:
        try:
            return self.datasource.get_posters(content)
        except Failure as error:
            raise error

    def result_search(self, content: bytes) -> List[ResultSearchModel]:
        try:
            return self.datasource.result_search(content)
        except Failure as error:
            raise error
