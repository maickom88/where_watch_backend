# type: ignore
from typing import List
from src.data.models.poster_model import PosterModel
from src.domain.errors.failures import Failure
from src.core.usecases.usecases import NoParams
from src.external.webdriver_scraping import WebDiverScraping
from src.data.repositories import scraping_repository_impl
from src.domain.usecases.get_posters_usecase import GetPostersUsecase
from fastapi.routing import APIRouter
from fastapi.responses import JSONResponse
router = APIRouter()


psoters_router = {
    "router": router,
    "prefix": "/posters",
    "tags": ["Posters"],
}


@router.get(path='', response_model=List[PosterModel])
async def get_posters():
    url = 'https://www.justwatch.com/br?providers=dnp,gop,nfx,prv'
    usecase = setUp(url)
    try:
        result = usecase.call(NoParams())
        posters = [PosterModel.toMap(poster) for poster in result]
        return posters
    except Failure as e:
        return JSONResponse(
            status_code=500,
            content={
                "message": e.get_message_error()
            })


def setUp(url: str) -> GetPostersUsecase:
    datasource = WebDiverScraping(url=url)
    repository = scraping_repository_impl.ScrapingRepositoryImpl(datasource)
    usecase = GetPostersUsecase(repository)
    return usecase
