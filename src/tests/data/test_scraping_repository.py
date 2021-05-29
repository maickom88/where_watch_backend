from src.domain.errors.failures import Failure, NotFoundFailure
from src.data.repositories import scraping_repository_impl
from src.data.datasources.scraping_datasource import ScrapingDatasource
from src.domain.entities.poster_entity import PosterEntity
from unittest.mock import Mock

datasource = Mock(spec=ScrapingDatasource)
post = PosterEntity(url="http/algumacoisa", image="açgi", type_poster="aosd")
repository = scraping_repository_impl.ScrapingRepositoryImpl(datasource)
bytes = b"0x410x420x43"


def test_should_return_list_posts():
    datasource.get_posters.return_value = [post]
    result = repository.get_posters(bytes)

    assert isinstance(result, list)
    assert len(result) > 0
    assert isinstance(result[0], PosterEntity)
    posts = result[0]
    assert posts.url == post.url


def test_should_return_list_posts_empty():
    datasource.get_posters.return_value = []
    result = repository.get_posters(bytes)

    assert isinstance(result, list)
    assert result == []


def test_should_return_failure():
    datasource.get_posters.side_effect = NotFoundFailure()

    try:
        result = repository.get_posters(bytes)
    except Failure as error:
        result = error

    assert isinstance(result, Failure)
    assert isinstance(result, NotFoundFailure)
    assert result.get_message_error() == "Nada encontrado!"
