# Importing required libs
import os
from keras.models import load_model
from keras.utils import img_to_array
import numpy as np
from PIL import Image

# Determine the script's directory and construct the model file path
script_dir = os.path.dirname(os.path.abspath(__file__))
model_filename = "digit_model.h5"
model_path = os.path.join(script_dir, model_filename)

# Loading model
model = load_model(model_path)

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

