from fastapi import APIRouter, HTTPException
from data import plants, response

router = APIRouter()


@router.get(
    "/{plant_id}",
    name="Search Plant",
    description="Search Plants",
    response_model=response.DetailModel,
)
async def get_plant(plant_id: int):
    try:
        if plant_id >= len(plants.plants):
            raise HTTPException(status_code=404, detail="Plant not found")

        result = plants.plants[plant_id]

        if not result:
            raise HTTPException(status_code=404, detail="Plant not found")

        return {"data": result}
    except HTTPException as e:
        raise e
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
