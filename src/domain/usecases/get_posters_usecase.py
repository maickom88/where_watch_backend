# type: ignore
import logging
from src.domain.errors.failures import DomainFailure, Failure
from src.domain.repositories.scraping_repository import ScrapingRepository
from src.domain.entities.poster_entity import PosterEntity
from src.core.usecases.usecases import NoParams, Usecase
from typing import List, Type


class GetPostersUsecase(Usecase[NoParams, List[PosterEntity]]):
    def __init__(self, scrapingRepository: Type[ScrapingRepository]):
        self.scrapingRepository = scrapingRepository

    def call(self, input: NoParams) -> List[PosterEntity]:
        try:
            return self.scrapingRepository.get_posters()
        except Failure as error:
            logging.exception(f"Failed to retrieve posts:${error}")
            raise error
        except Exception:
            logging.exception("Failed to retrieve posts: DomainError")
            # noqa: W292
            raise DomainFailure()
