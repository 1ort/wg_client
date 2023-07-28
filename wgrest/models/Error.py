from typing import *

from pydantic import BaseModel, Field


class Error(BaseModel):
    """
    None model

    """

    code: str = Field(alias="code")

    message: str = Field(alias="message")

    detail: Optional[str] = Field(alias="detail", default=None)
