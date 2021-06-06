# type: ignore
from typing import List
from src.core.enums.providers import Providers


base_url = "https://www.justwatch.com"
providers = [
    Providers.GLOBOPLAY,
    Providers.NETFLIX,
    Providers.PRIMEVIDEO,
    Providers.DISNEYPLUS
]


class UrlConst(object):

    @staticmethod
    def posters_endpoint(prov: List[Providers]) -> str:
        if len(prov) <= 0 or prov is None:
            prov = providers
        string_providers = assemble_providers(prov)
        return f'{base_url}/br?providers={string_providers}'

    @staticmethod
    def details_endpoint(link: str) -> str:
        return f'{base_url}{link}'


def assemble_providers(providers: List[Providers]) -> str:
    string_providers = ''
    print(providers)
    for provider in providers:
        string_providers += f'{provider.value},'
    return string_providers
