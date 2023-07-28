from typing import *

from pydantic import BaseModel, Field


class DeviceOptions(BaseModel):
    """
    None model
        Device options

    """

    allowed_ips: List[str] = Field(alias="allowed_ips")

    dns_servers: List[str] = Field(alias="dns_servers")

    host: str = Field(alias="host")
