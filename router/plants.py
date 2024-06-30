from fastapi import APIRouter, HTTPException
from data import plants, response

router = APIRouter()


@router.get(
    "",
    name="List Plants",
    description="List Plants",
    response_model=response.SearchModel,
)
async def list_plants():
    try:
        plant_results = []
        for index, plant in enumerate(plants.plants):
            plant_results.append({"index": index, **plant.to_dict()})

        return {"data": plant_results}
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get(
    "/{plant_id}",
    name="Get Plant",
    description="Get Plant by Id",
    response_model=response.DetailModel,
)
async def get_plant(plant_id: int):
    try:
        if plant_id >= len(plants.plants):
            raise HTTPException(status_code=404, detail="Plant not found")

        result = plants.plants[plant_id].to_dict()

        if not result:
            raise HTTPException(status_code=404, detail="Plant not found")

        return {"data": {"index": plant_id, **result}}
    except HTTPException as e:
        raise e
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
