# type: ignore
from pydantic.main import BaseModel
from src.data.models.poster_model import PosterModel
from src.domain.entities.details_entity import DetailsEntity
from typing import List, Optional


class DetailsModel(BaseModel, DetailsEntity, object):
    banners: list
    poster_image: str
    type_poster: Optional[str] = None
    runtime: str
    sinopse: str
    title: str
    year: str
    seansons: Optional[List[Optional[PosterModel]]] = None
    genders: List[str]
    providers: List[str]

    @staticmethod
    def toMap(details: DetailsEntity) -> dict:
        sinopse = ''.join(details.sinopse)
        seansons = None
        if details.seansons is not None:
            seansons = [PosterModel.toMap(seanson)
                        for seanson in details.seansons]
        return {
            'type_poster': details.type_poster,
            'poster_image': details.poster_image,
            'banners': details.banners,
            'genders': details.genders,
            'providers': details.providers,
            'runtime': details.runtime,
            'seansons': seansons,
            'sinopse': sinopse,
            'title': details.title,
            'year': details.year,
        }
