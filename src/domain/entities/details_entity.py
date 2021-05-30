# type: ignore
from src.domain.entities.poster_entity import PosterEntity
from typing import List


class DetailsEntity:
    banners: list[str]
    sinopse: str
    poster_image: str
    type_poster: str
    runtime: str
    title: str
    year: str
    age_rating: str
    seansons: List[PosterEntity]
    gender: str
    providers: list[str]

    def __init__(self,
                 title: str,
                 banners: list[str],
                 type_poster: str,
                 poster_image: str,
                 age_rating: str,
                 runtime: str,
                 year: str,
                 sinopse: str,
                 providers: list[str],
                 seansons: List[PosterEntity],
                 gender: str):
        self.title = title
        self.year = year
        self.seansons = seansons
        self.gender = gender
        self.runtime = runtime
        self.age_rating = age_rating
        self.banners = banners,
        self.sinopse = sinopse,
        self.type_poster = type_poster
        self.poster_image = poster_image
        self.providers = providers
        # noqa: W292
