# type: ignore
from typing import List
from src.domain.entities.poster_entity import PosterEntity


class ResultSearchEntity:
    title: str
    year: str
    providers: List[str]
    posters: PosterEntity

    def __init__(self,
                 title: str,
                 providers: List[str],
                 posters: PosterEntity,
                 year: str):
        self.title = title
        self.year = year
        self.providers = providers
        self.posters = posters
        # noqa: W292
