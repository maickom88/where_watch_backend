# type: ignore
import logging
from src.domain.errors.failures import DomainFailure, Failure
from src.core.usecases.usecases import Usecase
from src.domain.repositories.http_repository import HttpRepository
from typing import Type


class GetContentPage(Usecase[str, str]):
    def __init__(self, http_repository: Type[HttpRepository]):
        self.http_repository = http_repository

    def call(self, input: str) -> bytes:
        try:
            return self.http_repository.get_content_page(url=input)
        except Failure as error:
            logging.exception(f"Failed to retrieve content html page: {error}")
            raise error
        except Exception:
            logging.exception(
                "Failed to retrieve content html page: DomainError")
            # noqa: W292
            raise DomainFailure()
