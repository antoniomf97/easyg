from pydantic import BaseModel
from typing import List


class InputData(BaseModel):
    values: List[float]
