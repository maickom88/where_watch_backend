from src.domain.errors.failures import Failure, NotFoundFailure
from src.domain.errors.failures import ResponseFailure
from src.data.datasources.http_datasource import HttpDatasource
from src.data.repositories.http_repository_impl import HttpReposiroyImpl
from unittest.mock import Mock

datasource = Mock(spec=HttpDatasource)
repository = HttpReposiroyImpl(datasource)
content: str = '''
<div>test</div>
'''


def test_should_return_content_html():
    datasource.get_content_page.return_value = content
    result = repository.get_content_page(url='any')

    assert isinstance(result, str)
    assert len(result) > 0
    assert result == content


def test_should_return_NotFoundFailure():
    datasource.get_content_page.side_effect = NotFoundFailure()

    try:
        result = repository.get_content_page(url='any')
    except Failure as error:
        result = error

    assert isinstance(result, Failure)
    assert isinstance(result, NotFoundFailure)
    assert result.get_message_error() == "Nada encontrado!"


def test_should_return_ResponseFailure():
    datasource.get_content_page.side_effect = ResponseFailure()

    try:
        result = repository.get_content_page(url='any')
    except Failure as error:
        result = error

    assert isinstance(result, Failure)
    assert isinstance(result, ResponseFailure)
    assert result.get_message_error() == "Error ao tentar obter conteúdo!"
