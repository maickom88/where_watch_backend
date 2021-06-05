# type: ignore
from src.domain.entities.poster_entity import PosterEntity
from typing import List, Optional


class DetailsEntity:
    banners: list
    poster_image: str
    sinopse: str
    type_poster: Optional[str] = None
    runtime: str
    title: str
    year: str
    seansons: Optional[List[Optional[PosterEntity]]] = None
    genders: List[str]
    providers: List[str]

    def __init__(self,
                 title: str,
                 banners: list,
                 poster_image: str,
                 runtime: str,
                 year: str,
                 sinopse: str,
                 providers: List[str],
                 genders: List[str],
                 seansons: Optional[List[Optional[PosterEntity]]] = None,
                 type_poster: Optional[str] = None
                 ):
        self.title = title
        self.year = year
        self.seansons = seansons
        self.genders = genders
        self.runtime = runtime
        self.banners = banners,
        self.sinopse = sinopse,
        self.type_poster = type_poster
        self.poster_image = poster_image
        self.providers = providers
        # noqa: W292
