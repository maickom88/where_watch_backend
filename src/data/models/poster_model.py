# type: ignore
from typing import Optional
from pydantic.main import BaseModel
from src.domain.entities.poster_entity import PosterEntity


class PosterModel(BaseModel, PosterEntity, object):
    url: str
    image: str
    type_poster: Optional[str] = None

    @staticmethod
    def toMap(poster: PosterEntity) -> dict:
        return {
            'url': poster.url,
            'image': poster.image,
            'type_poster': poster.type_poster,
        }
