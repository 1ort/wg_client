from typing import *

from pydantic import BaseModel, Field


class Device(BaseModel):
    """
    None model
        Information about wireguard device.

    """

    name: str = Field(alias="name")

    listen_port: int = Field(alias="listen_port")

    public_key: str = Field(alias="public_key")

    firewall_mark: int = Field(alias="firewall_mark")

    networks: List[str] = Field(alias="networks")

    peers_count: int = Field(alias="peers_count")

    total_receive_bytes: int = Field(alias="total_receive_bytes")

    total_transmit_bytes: int = Field(alias="total_transmit_bytes")
