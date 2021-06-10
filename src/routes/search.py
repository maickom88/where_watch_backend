# type: ignore
from typing import List
from src.data.models.result_search_model import ResultSearchModel
from src.domain.usecases.get_search import GetSearch
from src.core.constants.url_consts import UrlConst
from src.domain.errors.failures import Failure
from src.core.usecases.usecases import NoParams
from src.data.models.search_params_model import SearchParams
from src.external.webdriver_scraping import WebDiverScraping
from src.data.repositories import scraping_repository_impl
from fastapi.routing import APIRouter
from fastapi.responses import JSONResponse
router = APIRouter()


search_router = {
    "router": router,
    "prefix": "/search",
    "tags": ["Search"],
}


@router.post(path='',  response_model=List[ResultSearchModel])
async def get_posters(search: SearchParams):

    url = UrlConst.search_endpoint(search.search, search.providers)

    usecase = setUp(url)
    try:
        result = usecase.call(NoParams())
        posters = [ResultSearchModel.toMap(poster) for poster in result]
        return posters
    except Failure as e:
        return JSONResponse(
            status_code=500,
            content={
                "message": e.get_message_error()
            })


def setUp(url: str) -> GetSearch:
    datasource = WebDiverScraping(url=url)
    repository = scraping_repository_impl.ScrapingRepositoryImpl(datasource)
    usecase = GetSearch(repository)
    return usecase
