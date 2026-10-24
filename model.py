
"""Image preprocessing and prediction utilities for digit recognition."""

from keras.models import load_model
from keras.utils import img_to_array
import numpy as np
from PIL import Image

# Load the trained model.
model = load_model("digit_model.h5")


def preprocess_img(img_path):
    """Convert an uploaded image into a normalized model input."""
    with Image.open(img_path) as op_img:
        op_img = op_img.convert("RGB")
        img_resize = op_img.resize((224, 224))
        img2arr = img_to_array(img_resize) / 255.0
        img_reshape = img2arr.reshape(1, 224, 224, 3)
        return img_reshape



def predict_result(predict):
    """Return the predicted digit class for a preprocessed image."""
    pred = model.predict(predict)
    return np.argmax(pred[0], axis=-1)
