from fastapi import FastAPI
from app.core.config import get_settings
from app.api.v1.routes import api_router

def create_application() -> FastAPI:
    settings = get_settings()
    app = FastAPI(title=settings.APP_NAME)
    app.include_router(api_router, prefix=settings.API_V1_PREFIX)
    return app

app = create_application()