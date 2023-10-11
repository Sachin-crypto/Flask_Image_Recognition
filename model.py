"""
This module is responsible for loading the model and predicting the result.

This module is responsible for loading the model and predicting the result.

Author: [Your Name]
Date: [Current Date]
"""
# Importing required libs
from __future__ import annotations

import numpy as np
from keras.models import load_model
from keras.utils import img_to_array
from PIL import Image

# Loading model
model = load_model("digit_model.h5")


# Preparing and pre-processing the image
def preprocess_img(img_path):
    """
    Pre-process the image.

    This function is responsible for pre-processing the image.

    Args:
        img_path (str): The path to the image file.

    Returns:
        np.array: The image in a numpy array.
    """
    op_img = Image.open(img_path)
    img_resize = op_img.resize((224, 224))
    img2arr = img_to_array(img_resize) / 255.0
    img_reshape = img2arr.reshape(1, 224, 224, 3)
    return img_reshape


# Predicting function
def predict_result(predict):
    """ 
    Predicts the result of the image.

    This function is responsible for predicting the result of the image.

    Args:
        predict (np.array): The image in a numpy array.

    Returns:
        int: The predicted result.
    """
    pred = model.predict(predict)
    return np.argmax(pred[0], axis=-1)
