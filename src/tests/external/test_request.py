# type: ignore
from src.external.requests import Requests

url: str = "https://en.wikipedia.org/wiki/Web_scraping"


def test_should_return_content_html():
    http = Requests()
    result = http.get_content_page(url)
    assert isinstance(result, bytes)


def test_should_return_error():
    http = Requests()
    result = http.get_content_page(url)
    assert isinstance(result, bytes)
