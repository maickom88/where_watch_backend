# type: ignore
from typing import List
from src.core.enums.providers import Providers


base_url = "https://www.justwatch.com"


class UrlConst(object):
    providers = [
        Providers.GLOBOPLAY,
        Providers.NETFLIX,
        Providers.PRIMEVIDEO,
        Providers.DISNEYPLUS
    ]

    @staticmethod
    def posters_endpoint(providers: List[Providers] = providers) -> str:
        string_providers = assemble_providers(providers)
        return f'{base_url}/br?providers={string_providers}'

    @staticmethod
    def details_endpoint(link: str) -> str:
        return f'{base_url}{link}'


def assemble_providers(providers: List[Providers]) -> str:
    string_providers = ''
    for provider in providers:
        string_providers += f'{provider.value},'
    return string_providers
