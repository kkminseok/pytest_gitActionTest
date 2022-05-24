from datetime import datetime, time

from pydantic import BaseModel


class AppServiceInformationResponse(BaseModel):
    title: str
    description: str
    server_time: time
    open_time: time
    close_time: time

