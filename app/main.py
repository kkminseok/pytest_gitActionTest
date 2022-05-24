from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.routes.api import router


def get_application() -> FastAPI:
    application = FastAPI()
    application.include_router(router)
    cors(application)
    return application


def cors(fast_app):
    fast_app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"],
    )


app: FastAPI = get_application()
