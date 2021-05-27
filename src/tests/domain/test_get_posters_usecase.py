# type: ignore
from src.domain.errors.failures import DomainFailure, Failure, NotFoundFailure
from src.domain.repositories.scraping_repository import ScrapingRepository
from src.domain.entities.poster_entity import PosterEnitity
from src.core.usecases.usecases import NoParams
from src.domain.usecases.get_posters_usecase import GetPostersUsecase
from unittest.mock import Mock

repository = Mock(spec=ScrapingRepository)
post = PosterEnitity(url="http/algumacoisa", image="açgi", type_poster="aosd")


def test_should_return_list_posts():
    repository.get_posters.return_value = [post]
    usecase = GetPostersUsecase(repository)
    result = usecase.call(input=NoParams())

    assert isinstance(result, list)
    assert len(result) > 0
    assert isinstance(result[0], PosterEnitity)
    posts = result[0]
    assert posts.url == post.url


def test_should_return_list_posts_empty():
    repository.get_posters.return_value = []
    usecase = GetPostersUsecase(repository)
    result = usecase.call(input=NoParams())

    assert isinstance(result, list)
    assert result == []


def test_should_return_exception_domain_error():
    repository.get_posters.side_effect = Exception("ok")
    usecase = GetPostersUsecase(repository)
    try:
        result = usecase.call(input=NoParams())
    except Exception:
        result = DomainFailure()

    assert isinstance(result, Failure)
    assert isinstance(result, DomainFailure)
    assert result.get_message_error() == "Error de dominio"


def test_should_return_failure():
    repository.get_posters.side_effect = NotFoundFailure()
    usecase = GetPostersUsecase(repository)
    try:
        result = usecase.call(input=NoParams())
    except Failure as error:
        result = error

    assert isinstance(result, Failure)
    assert isinstance(result, NotFoundFailure)
    assert result.get_message_error() == "Nada encontrado!"
