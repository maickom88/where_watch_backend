# type: ignore
import logging
from src.data.datasources.http_datasource import HttpDatasource
from src.domain.errors.failures import NotFoundFailure, Failure
from src.domain.errors.failures import ResponseFailure
import requests


class Requests(HttpDatasource):
    def get_content_page(self, url: str) -> bytes:
        try:
            response = requests.get(url)
            if response.status_code == 404:
                raise NotFoundFailure()
            if response.status_code != 200:
                raise ResponseFailure()
            return response.content
        except Failure as error:
            logging.exception(
                f"Failed to retrieve requests content html: {error}")
            raise error
        except Exception:
            logging.exception("Failed to retrieve generic exception")
            raise ResponseFailure()
