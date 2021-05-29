from abc import ABC, abstractmethod


class HttpDatasource(ABC):
    @abstractmethod
    def get_content_page(self, url: str) -> bytes:
        pass
