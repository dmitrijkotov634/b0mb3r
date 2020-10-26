from typing import Optional

from pydantic import BaseModel


class StatusModel(BaseModel):
    started_at: Optional[str]
    currently_at: Optional[int]
    end_at: Optional[int]


class AttackModel(BaseModel):
    number_of_cycles: int
    phone: str
