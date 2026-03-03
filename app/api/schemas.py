from pydantic import BaseModel
from typing import Optional, List

class Filter(BaseModel):
    column: str
    operator: str
    value: int | float | str

class Metric(BaseModel):
    column: str
    aggregation: str

class StructuredQuery(BaseModel):
    filters: Optional[List[Filter]] = []
    groupby: Optional[List[str]] = []
    metrics: Optional[List[Metric]] = []

class NaturalLangauageQuery(BaseModel):
    query: str