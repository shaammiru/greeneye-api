from fastapi import APIRouter, Query, HTTPException
from data import plants, response
from service import search

router = APIRouter()


@router.post(
    "",
    name="Search Plant",
    description="Search Plants",
    response_model=response.SearchModel,
)
async def search_plants(keyword: str = Query(..., min_length=3, max_length=50)):
    try:
        results = search.search_plants(keyword)
        plant_results = []

        for index in results:
            plant_results.append({"index": index, **plants.plants[index].to_dict()})

        return {"data": plant_results}
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
