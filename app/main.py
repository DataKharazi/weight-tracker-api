from fastapi import FastAPI
from app.schemas import WeightEntryCreate, WeightEntryResponse

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/weights", response_model=WeightEntryResponse)
def create_weight_entry(weight_entry: WeightEntryCreate):
    return {
        "message": "Weight entry received",
        "weight_kg": weight_entry.weight_kg
    }