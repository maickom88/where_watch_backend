# type: ignore
from pydantic.main import BaseModel
from src.data.models.poster_model import PosterModel
from typing import List, Optional
from src.domain.entities.result_search_entity import ResultSearchEntity


class ResultSearchModel(BaseModel, ResultSearchEntity, object):
    title: str
    year: str
    providers: List[str]
    posters: Optional[PosterModel] = None

    @staticmethod
    def toMap(result: ResultSearchEntity) -> dict:
        return {
            'title': result.title,
            'year': result.year,
            'providers': result.providers,
            'posters': PosterModel.toMap(result.posters)
        }
