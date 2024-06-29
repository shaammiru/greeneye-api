from fastapi import APIRouter, File, UploadFile, HTTPException
from tensorflow.keras.models import load_model
from service import predict
from data import plants, response

model = load_model("models/plant_organs_classifier.keras")
organs_classname = ["flowers", "fruits", "habits", "leafs"]
img_height, img_width = 224, 224

router = APIRouter()


@router.post(
    "/",
    name="Predict Image",
    description="Predict Plant Image",
    response_model=response.PredictModel,
)
async def predict_image(file: UploadFile = File(...)):
    try:
        img_bytes = await file.read()
        index, organs, classname, accuracy = predict.predict_plants(img_bytes)

        return {
            "data": {
                "index": index,
                "organs": organs,
                "classname": classname,
                "accuracy": accuracy,
                "plants": plants.plants[index],
            }
        }
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
