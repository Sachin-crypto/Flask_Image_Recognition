# Importing required libs
from keras.models import load_model
from keras.utils import img_to_array
import numpy as np
from PIL import Image
import os

script_dir = os.path.dirname(__file__)
model_file = "digit_model.h5"
model_path = os.path.join(script_dir, model_file)


# Preparing and pre-processing the image
def preprocess_img(img_path):
    op_img = Image.open(img_path)
    img_resize = op_img.resize((224, 224))
    img2arr = img_to_array(img_resize) / 255.0
    img_reshape = img2arr.reshape(1, 224, 224, 3)
    return img_reshape


# Predicting function
def predict_result(predict):
    pred = model.predict(predict)
    return np.argmax(pred[0], axis=-1)
