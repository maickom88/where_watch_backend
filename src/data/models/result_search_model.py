# type: ignore
from src.data.models.poster_model import PosterModel
from typing import List
from src.domain.entities.result_search_entity import ResultSearchEntity


class ResultSearchModel(ResultSearchEntity):
    title: str
    year: str
    providers: List[str]
    posters: PosterModel

    def __init__(self,
                 title: str,
                 providers: List[str],
                 posters: PosterModel,
                 year: str):
        self.title = title
        self.year = year
        self.providers = providers
        self.posters = posters
        # noqa: W292

        def toString(self):
            print(
                f'''
            TITLE: {self.title}\n
            YEAR: {self.year}\n
            POSTERS: {len(self.posters)}\n
            PROVIDERS: {self.providers}''')
