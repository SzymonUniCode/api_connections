from typing import Dict, List
from pydantic import BaseModel


class DataPointSchema(BaseModel):
    date: str
    value: float


class ComparisonPayloadSchema(BaseModel):
    source_a: str
    source_b: str
    start_date: str
    end_date: str


class ComparisonOutputSchema(BaseModel):
    data: Dict[str, List[DataPointSchema]]