import datetime

from app.models.domain.app_info import AppServiceInformation


class MockAppServiceRepository:
    async def get_app_service_information(self) -> AppServiceInformation:
        return AppServiceInformation(
            title="야근병동",
            description="v1",
            open_time=datetime.time(18, 0, 0),
            close_time=datetime.time(2, 0, 0)
        )

