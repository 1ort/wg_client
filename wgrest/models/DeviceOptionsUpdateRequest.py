from typing import *

from pydantic import BaseModel, Field


class DeviceOptionsUpdateRequest(BaseModel):
    """
    None model
        Device options

    """

    allowed_ips: Optional[List[str]] = Field(alias="allowed_ips", default=None)

    dns_servers: Optional[List[str]] = Field(alias="dns_servers", default=None)

    host: Optional[str] = Field(alias="host", default=None)
