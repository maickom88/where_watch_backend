# type: ignore
import logging
from src.domain.errors.failures import DomainFailure, Failure
from src.domain.repositories.scraping_repository import ScrapingRepository
from src.domain.entities.details_entity import DetailsEntity
from src.core.usecases.usecases import Usecase
from typing import Type


class GetDetails(Usecase[bytes, DetailsEntity]):
    def __init__(self, scrapingRepository: Type[ScrapingRepository]):
        self.scrapingRepository = scrapingRepository

    def call(self, input: bytes) -> DetailsEntity:
        try:
            return self.scrapingRepository.get_posters(input)
        except Failure as error:
            logging.exception(f"Failed to retrieve posts:${error}")
            raise error
        except Exception:
            logging.exception("Failed to retrieve posts: DomainError")
            # noqa: W292
            raise DomainFailure()
