from fastapi import FastAPI, HTTPException
from app.schemas import WeightEntryCreate, WeightEntryResponse

app = FastAPI()

weight_entries = []


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/weights", response_model=WeightEntryResponse)
def create_weight_entry(weight_entry: WeightEntryCreate):
    new_id = len(weight_entries) + 1

    new_entry = {
        "id": new_id,
        "weight_kg": weight_entry.weight_kg
    }

    weight_entries.append(new_entry)

    return new_entry


@app.get("/weights", response_model=list[WeightEntryResponse])
def get_weight_entries():
    return weight_entries


@app.get("/weights/{entry_id}", response_model=WeightEntryResponse)
def get_weight_entry(entry_id: int):
    for entry in weight_entries:
        if entry["id"] == entry_id:
            return entry

    raise HTTPException(status_code=404, detail="Weight entry not found")