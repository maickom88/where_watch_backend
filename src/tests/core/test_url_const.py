# type: ignore
from src.core.enums.providers import Providers
from src.core.constants.url_consts import UrlConst


def test_should_return_many_providers():
    result = UrlConst.posters_endpoint([Providers.GLOBOPLAY])
    assert isinstance(result, str)


def test_should_return_one_providers():
    result = UrlConst.posters_endpoint([Providers.GLOBOPLAY])
    assert isinstance(result, str)
