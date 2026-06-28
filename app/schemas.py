from pydantic import BaseModel, Field


class WeightEntryCreate(BaseModel):
    weight_kg: float = Field(gt=0)


class WeightEntryResponse(BaseModel):
    message: str
    weight_kg: float