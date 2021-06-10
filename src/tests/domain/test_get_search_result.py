# type: ignore
from src.domain.errors.failures import DomainFailure, Failure
from src.domain.errors.failures import NotFoundFailure
from src.domain.repositories.scraping_repository import ScrapingRepository
from src.domain.entities.poster_entity import PosterEntity
from src.domain.entities.result_search_entity import ResultSearchEntity
from src.domain.usecases.get_search import GetSearch
from unittest.mock import Mock

repository = Mock(spec=ScrapingRepository)
usecase = GetSearch(repository)
post = PosterEntity(url="http/algumacoisa", image="açgi", type_poster="aosd")
resultentity = ResultSearchEntity(
    title="test",
    posters=post,
    providers=['url'],
    year='2021')

bytes = b"0x410x420x43"


def test_should_return_list_result_entity():
    repository.result_search.return_value = [resultentity]
    result = usecase.call(input=bytes)

    assert isinstance(result, list)
    assert len(result) > 0
    assert isinstance(result[0], ResultSearchEntity)
    posts = result[0].posters
    assert result[0].title == resultentity.title
    assert posts.url == post.url


def test_should_return_list_result_empty():
    repository.result_search.return_value = []
    result = usecase.call(input=bytes)

    assert isinstance(result, list)
    assert result == []


def test_should_return_exception_domain_error():
    repository.result_search.side_effect = Exception("ok")
    try:
        result = usecase.call(input=bytes)
    except Exception:
        result = DomainFailure()

    assert isinstance(result, Failure)
    assert isinstance(result, DomainFailure)
    assert result.get_message_error() == "Error de dominio"


def test_should_return_failure():
    repository.result_search.side_effect = NotFoundFailure()
    try:
        result = usecase.call("")
    except Failure as error:
        result = error

    assert isinstance(result, Failure)
    assert isinstance(result, NotFoundFailure)
    assert result.get_message_error() == "Nada encontrado!"
