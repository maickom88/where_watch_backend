# type: ignore
from src.domain.entities.poster_entity import PosterEntity
from src.external.requests import Requests
from src.data.repositories.http_repository_impl import HttpReposiroyImpl
from src.domain.usecases.get_content_page import GetContentPage
from src.external.webdriver_scraping import WebDiverScraping
from bs4 import BeautifulSoup
from src.external.bs4_scraping import Bs4


datasource_repository = Requests()
http_repository = HttpReposiroyImpl(datasource_repository)
usecase = GetContentPage(http_repository)
url = "https://www.justwatch.com/br?providers=dnp,gop,nfx,prv"
url2 = 'https://www.justwatch.com/br/busca?providers=dnp,gop,nfx,prv&q=fri'
url3 = 'https://www.justwatch.com/br/filme/interestelar'


def test_should_return_list_posts():
    result = usecase.call(input=url)
    scraping = Bs4(BeautifulSoup(result, 'html.parser'))
    result = scraping.get_posters()

    assert isinstance(result, list)
    assert len(result) > 0
    assert isinstance(result[0], PosterEntity)


def test_should_return_list_results():
    scraping = WebDiverScraping(url2)
    result = scraping.result_search()
    assert isinstance(result, list)


def test_should_return_details_page():
    scraping = WebDiverScraping(url3)
    result = scraping.get_details()
    print(result)
