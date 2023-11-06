# Importing required libs
from tensorflow.keras.models import load_model
from keras.utils import img_to_array
from PIL import Image
import os
import numpy as np

# Define the relative path to the "digit_model.h5" file
RELATIVE_PATH = 'digit_model.h5'

# Get the absolute path to the file
file_path = os.path.join(os.path.dirname(__file__), RELATIVE_PATH)

# Now you can work with the file using file_path
# For example, if you want to load the model (assuming it's an h5 file):
model = load_model(file_path)

# You can use the model in your script


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

