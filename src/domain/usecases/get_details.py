# type: ignore
import logging
from src.domain.errors.failures import DomainFailure, Failure
from src.domain.repositories.scraping_repository import ScrapingRepository
from src.domain.entities.details_entity import DetailsEntity
from src.core.usecases.usecases import NoParams, Usecase
from typing import Type


class GetDetails(Usecase[NoParams, DetailsEntity]):
    def __init__(self, scrapingRepository: Type[ScrapingRepository]):
        self.scrapingRepository = scrapingRepository

    def call(self, input: NoParams) -> DetailsEntity:
        try:
            return self.scrapingRepository.get_details()
        except Failure as error:
            logging.exception(f"Failed to retrieve details page: {error}")
            raise error
        except Exception:
            logging.exception("Failed to retrieve details: DomainError")
            # noqa: W292
            raise DomainFailure()
