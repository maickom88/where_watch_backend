# type: ignore
from src.core.constants.url_consts import UrlConst
from src.data.models.details_model import DetailsModel
from src.domain.errors.failures import Failure
from src.core.usecases.usecases import NoParams
from src.external.webdriver_scraping import WebDiverScraping
from src.data.repositories import scraping_repository_impl
from src.domain.usecases.get_details import GetDetails
from fastapi.routing import APIRouter
from fastapi.responses import JSONResponse
router = APIRouter()


details_router = {
    "router": router,
    "prefix": "/details",
    "tags": ["Details Poster"],
}


@router.get(path='', response_model=DetailsModel)
async def get_details_poster(link: str):
    if link is None:
        return JSONResponse(
            status_code=404,
            content={
                "message": 'link is empty!'
            })
    url = UrlConst.details_endpoint(link)
    usecase = setUp(url)
    try:
        result = usecase.call(NoParams())
        details = DetailsModel.toMap(result)
        return details
    except Failure as e:
        return JSONResponse(
            status_code=500,
            content={
                "message": e.get_message_error()
            })


def setUp(url: str) -> GetDetails:
    datasource = WebDiverScraping(url=url)
    repository = scraping_repository_impl.ScrapingRepositoryImpl(datasource)
    usecase = GetDetails(repository)
    return usecase
