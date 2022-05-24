import datetime
from datetime import time

from fastapi import Depends

from app.db.repositories.app_info import MockAppServiceRepository
from app.models.io.app_info import AppServiceInformationResponse


async def get_app_service_information(
    app_service_repo: MockAppServiceRepository = Depends()
):
    info = await app_service_repo.get_app_service_information()
    server_time = datetime.datetime.now().time()
    return AppServiceInformationResponse(
        title=info.title,
        description=info.description,
        open_time=info.open_time,
        close_time=info.close_time,
        server_time=server_time
    )
