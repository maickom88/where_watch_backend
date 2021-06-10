# type: ignore
from abc import ABC, abstractmethod


class HttpRepository(ABC):
    @abstractmethod
    def get_content_page(self, url: str) -> bytes:
        pass  # noqa: W292
