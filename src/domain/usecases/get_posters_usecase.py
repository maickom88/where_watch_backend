from src.domain.entities.poster_entity import PosterEnitity
from src.core.usecases.usecases import NoParams, Usecase
from typing import List


class GetPostersUsecase(Usecase[NoParams, PosterEnitity]):
    def call(self, input:NoParams) -> List[PosterEnitity]:
        posters: List[PosterEnitity] = []
        poster = PosterEnitity(url="asdk", image="asd", type_poster="olá")
        posters.append(poster)
        return posters