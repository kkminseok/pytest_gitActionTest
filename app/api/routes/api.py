from fastapi import APIRouter

from app.api.routes import app_info

router = APIRouter()
router.include_router(app_info.router, tags=["app service information"], prefix="/service")
