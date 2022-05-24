from datetime import datetime, time

from pydantic import BaseModel


class AppServiceInformation(BaseModel):
    title: str
    description: str
    open_time: time
    close_time: time
