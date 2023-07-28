from typing import *

from pydantic import BaseModel, Field


class PeerCreateOrUpdateRequest(BaseModel):
    """
    None model
        Peer params that might be used due to creation or updation process

    """

    private_key: Optional[str] = Field(alias="private_key", default=None)

    public_key: Optional[str] = Field(alias="public_key", default=None)

    preshared_key: Optional[str] = Field(alias="preshared_key", default=None)

    allowed_ips: Optional[List[str]] = Field(alias="allowed_ips", default=None)

    persistent_keepalive_interval: Optional[str] = Field(alias="persistent_keepalive_interval", default=None)

    endpoint: Optional[str] = Field(alias="endpoint", default=None)
