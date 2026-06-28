from pydantic import BaseModel, Field


class WeightEntryCreate(BaseModel):
    weight_kg: float = Field(gt=0)


class WeightEntryResponse(BaseModel):
    id: int
    weight_kg: float