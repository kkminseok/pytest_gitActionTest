from fastapi import APIRouter, Depends

from app.models.io.app_info import AppServiceInformationResponse
from app.service.app_info import get_app_service_information

router = APIRouter()


@router.get(
    "",
    response_model=AppServiceInformationResponse,
)
async def get_service_app_information(
    info: AppServiceInformationResponse = Depends(get_app_service_information),
) -> AppServiceInformationResponse:
    return info
