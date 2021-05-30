# type: ignore
import logging
from src.domain.errors.failures import DomainFailure, Failure
from src.domain.repositories.scraping_repository import ScrapingRepository
from src.domain.entities.result_search_entity import ResultSearchEntity
from src.core.usecases.usecases import Usecase
from typing import List, Type


class GetSearch(Usecase[bytes, List[ResultSearchEntity]]):
    def __init__(self, scrapingRepository: Type[ScrapingRepository]):
        self.scrapingRepository = scrapingRepository

    def call(self, input: bytes) -> List[ResultSearchEntity]:
        try:
            return self.scrapingRepository.result_search(input)
        except Failure as error:
            logging.exception(f"Failed to retrieve search movies:${error}")
            raise error
        except Exception:
            logging.exception("Failed to retrieve search movies: DomainError")
            # noqa: W292
            raise DomainFailure()
