from src.domain.errors.failures import DomainFailure, Failure
from src.domain.errors.failures import NotFoundFailure, ResponseFailure
from unittest.mock import Mock
from src.domain.repositories.http_repository import HttpRepository
from src.domain.usecases.get_content_page import GetContentPage

repository = Mock(spec=HttpRepository)
usecase = GetContentPage(repository)
content: str = '''
<div>test</div>
'''


def test_should_return_content_str():
    repository.get_content_page.return_value = content

    result = usecase.call(input="any")
    assert isinstance(result, str)
    assert len(result) > 0
    assert result == content


def test_should_return_exception_domain_error():
    repository.get_content_page.side_effect = Exception("ok")
    try:
        result = usecase.call(input='any')
    except Exception:
        result = DomainFailure()

    assert isinstance(result, Failure)
    assert isinstance(result, DomainFailure)
    assert result.get_message_error() == "Error de dominio"


def test_should_return_not_found():
    repository.get_content_page.side_effect = NotFoundFailure()
    try:
        result = usecase.call(input='any')
    except Failure as error:
        result = error

    assert isinstance(result, Failure)
    assert isinstance(result, NotFoundFailure)
    assert result.get_message_error() == "Nada encontrado!"


def test_should_return_response_failure():
    repository.get_content_page.side_effect = ResponseFailure()
    try:
        result = usecase.call(input='any')
    except Failure as error:
        result = error

    assert isinstance(result, Failure)
    assert isinstance(result, ResponseFailure)
    assert result.get_message_error() == "Error ao tentar obter conteúdo!"
