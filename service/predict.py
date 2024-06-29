import io
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image

img_height, img_width = 224, 224
organs_model = load_model("models/plant_organs_classifier.keras")
flower_model = load_model("models/plant_flower_classifier.keras")
fruit_model = load_model("models/plant_fruit_classifier.keras")
habit_model = load_model("models/plant_habit_classifier.keras")
leaf_model = load_model("models/plant_leaf_classifier.keras")

organs_classname = ["Flowers", "Fruits", "Habits", "Leafs"]
plants_classname = [
    "Ananas comosus",
    "Artocarpus heterophyllus",
    "Carica papaya",
    "Cocos nucifera",
    "Musa spp",
    "Nephelium lappaceum",
    "Salacca zalacca",
]


def predict_plants(img_bytes: any):
    img = Image.open(io.BytesIO(img_bytes)).resize((img_height, img_width))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0

    predictions = organs_model.predict(img_array)
    predicted_class = np.argmax(predictions[0])
    predicted_classname = organs_classname[predicted_class]

    if predicted_classname == "Flowers":
        index, classname, accuracy = predict_flower(img_array)
    elif predicted_classname == "Fruits":
        index, classname, accuracy = predict_fruit(img_array)
    elif predicted_classname == "Habits":
        index, classname, accuracy = predict_habit(img_array)
    else:
        index, classname, accuracy = predict_leaf(img_array)

    return index, predicted_classname, classname, accuracy


def predict_flower(img_array: any):
    predictions = flower_model.predict(img_array)
    predicted_class = np.argmax(predictions[0])
    predicted_classname = plants_classname[predicted_class]
    prediction_accuracy = float(predictions[0][predicted_class])
    return int(predicted_class), predicted_classname, prediction_accuracy


def predict_fruit(img_array: any):
    predictions = fruit_model.predict(img_array)
    predicted_class = np.argmax(predictions[0])
    predicted_classname = plants_classname[predicted_class]
    prediction_accuracy = float(predictions[0][predicted_class])
    return int(predicted_class), predicted_classname, prediction_accuracy


def predict_habit(img_array: any):
    predictions = habit_model.predict(img_array)
    predicted_class = np.argmax(predictions[0])
    predicted_classname = plants_classname[predicted_class]
    prediction_accuracy = float(predictions[0][predicted_class])
    return int(predicted_class), predicted_classname, prediction_accuracy


def predict_leaf(img_array: any):
    predictions = leaf_model.predict(img_array)
    predicted_class = np.argmax(predictions[0])
    predicted_classname = plants_classname[predicted_class]
    prediction_accuracy = float(predictions[0][predicted_class])
    return int(predicted_class), predicted_classname, prediction_accuracy
