import logging
from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = "ws-ml-api"
    version: str = "1.0"
    api_prefix: str = ""
    debug: bool = True


settings = Settings()
logger = logging.getLogger()
