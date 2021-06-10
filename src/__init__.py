# type: ignore
from fastapi import FastAPI
from src.routes.details import details_router
from src.routes.posters import posters_router
from src.routes.search import search_router


def init_app():
    app = FastAPI(
        title="Where Watch",
        description="Where Watch API",
        version='1.0.4',
        redoc_url=None
    )
    app = config_app_routers(app)
    return app


def config_app_routers(app):
    routers = [
        details_router,
        posters_router,
        search_router
    ]
    routers.sort(key=lambda r: r.get("prefix"))
    [app.include_router(**r) for r in routers]
    return app
