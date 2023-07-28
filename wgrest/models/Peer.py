from typing import *

from pydantic import BaseModel, Field


class Peer(BaseModel):
    """
    None model
        Information about wireguard peer.

    """

    public_key: str = Field(alias="public_key")

    url_safe_public_key: str = Field(alias="url_safe_public_key")

    preshared_key: Optional[str] = Field(alias="preshared_key", default=None)

    allowed_ips: List[str] = Field(alias="allowed_ips")

    last_handshake_time: str = Field(alias="last_handshake_time")

    persistent_keepalive_interval: str = Field(alias="persistent_keepalive_interval")

    endpoint: str = Field(alias="endpoint")

    receive_bytes: int = Field(alias="receive_bytes")

    transmit_bytes: int = Field(alias="transmit_bytes")
