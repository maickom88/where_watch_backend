# type: ignore
from src.data.datasources.http_datasource import HttpDatasource
from src.domain.errors.failures import Failure
from typing import Type
from src.domain.repositories.http_repository import HttpRepository


class HttpReposiroyImpl(HttpRepository):
    def __init__(self, datasource: Type[HttpDatasource]):
        self.datasource = datasource

    def get_content_page(self, url: str) -> str:
        try:
            return self.datasource.get_content_page(url)
        except Failure as error:
            raise error
