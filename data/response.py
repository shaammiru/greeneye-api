from pydantic import BaseModel


class Plant(BaseModel):
    science_name: str
    en_name: str
    id_name: str
    description: str
    benefits: str
    effects: str
    tips: str


class Predict(BaseModel):
    index: int
    organs: str
    classname: str
    accuracy: float
    plants: Plant


class PredictModel(BaseModel):
    data: Predict


class DetailModel(BaseModel):
    data: Plant


class SearchModel(BaseModel):
    data: list[Plant]
