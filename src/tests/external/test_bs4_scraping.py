# type: ignore
from src.domain.entities.poster_entity import PosterEntity
from src.external.requests import Requests
from src.data.repositories.http_repository_impl import HttpReposiroyImpl
from src.domain.usecases.get_content_page import GetContentPage
from bs4 import BeautifulSoup
from src.external.bs4_scraping import Bs4

datasource_repository = Requests()
http_repository = HttpReposiroyImpl(datasource_repository)
usecase = GetContentPage(http_repository)
url = "https://www.justwatch.com/br?providers=dnp,gop,nfx,prv"


def test_should_return_list_posts():
    result = usecase.call(input=url)
    scraping = Bs4(BeautifulSoup(result, 'html.parser'))
    result = scraping.get_posters()

    assert isinstance(result, list)
    print(len(result))
    assert len(result) > 0
    assert isinstance(result[0], PosterEntity)
