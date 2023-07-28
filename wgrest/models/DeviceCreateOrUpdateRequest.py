from typing import *

from pydantic import BaseModel, Field


class DeviceCreateOrUpdateRequest(BaseModel):
    """
    None model
        Device params that might be used due to creation or updation process

    """

    name: Optional[str] = Field(alias="name", default=None)

    listen_port: Optional[int] = Field(alias="listen_port", default=None)

    private_key: Optional[str] = Field(alias="private_key", default=None)

    firewall_mark: Optional[int] = Field(alias="firewall_mark", default=None)

    networks: Optional[List[str]] = Field(alias="networks", default=None)
