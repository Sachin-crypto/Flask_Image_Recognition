"""
Model module for digit image classification.

This module provides:
- Loading a pre-trained Keras model.
- Preprocessing images for prediction.
- Predicting the digit from a preprocessed image.
"""

# Importing required libs
from keras.models import load_model
from keras.utils import img_to_array
import numpy as np
from PIL import Image

# Loading model
model = load_model("digit_model.h5")


def preprocess_img(img_path):
    """
    Preprocess an image for prediction.

    Steps:
    - Open the image using PIL.
    - Resize to (224, 224) pixels.
    - Convert the image to a NumPy array and normalize pixel values.
    - Reshape array to match model input shape (1, 224, 224, 3).

    Args:
        img_path (file-like object or str): Image file path or file stream.

    Returns:
        np.ndarray: Preprocessed image ready for prediction.
    """
    op_img = Image.open(img_path)
    img_resize = op_img.resize((224, 224))
    img2arr = img_to_array(img_resize) / 255.0
    img_reshape = img2arr.reshape(1, 224, 224, 3)
    return img_reshape


def predict_result(preprocessed_img):
    """
    Predict the class (digit) of a preprocessed image.

    Args:
        preprocessed_img (np.ndarray): Image processed by `preprocess_img`.

    Returns:
        int: Predicted digit (0-9).
    """
    pred = model.predict(preprocessed_img)
    return np.argmax(pred[0], axis=-1)
