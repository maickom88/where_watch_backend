# type: ignore
from fastapi import FastAPI
from src.routes.details import details_router


def init_app():
    app = FastAPI(
        title="Where Watch",
        description="Where Watch API",
        version='1.0.0',
        redoc_url=None
    )
    app = config_app_routers(app)
    return app


def config_app_routers(app):
    routers = [
        details_router,
    ]
    routers.sort(key=lambda r: r.get("prefix"))
    [app.include_router(**r) for r in routers]
    return app
