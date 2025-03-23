import fastapi
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from src import config
from src.config import logger, settings
from src.routers import monitor


def setup_app(settings_: config.Settings, lifespan_) -> None:
    app = fastapi.FastAPI(
        title=settings_.app_title,
        version=settings_.version,
        debug=settings_.debug,
        lifespan=lifespan_,
    )
    app.state.settings = settings_

    # Add exception handlers
    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(
        request: fastapi.Request, exc: StarletteHTTPException
    ) -> JSONResponse:
        query_params = request.path_params | dict(request.query_params)
        params = ",".join([f"{k}={v}" for k, v in query_params.items()])
        logger.error(f"[{params}] Error: {exc.detail}")

        return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})

    # include routers
    app.include_router(
        monitor.api_router,
        tags=["monitoring"],
        responses={404: {"description": "Not found"}},
    )

    return app


app = setup_app(settings, None)
