import fastapi


api_router = fastapi.APIRouter()


@api_router.get(
    "/healthcheck",
    tags=["utils"],
    summary="Dummy URL for healthchecks",
    response_description="OK with status 200",
)
async def healthcheck() -> str:
    return "OK"


@api_router.get(
    "/crash",
    tags=["utils"],
    summary="Endpoint for infrastructure tests",
    response_description="always 500",
)
async def test_app_crash() -> str:
    1 / 0
    return "OK"
