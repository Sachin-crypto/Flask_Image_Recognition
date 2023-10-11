"""
This script sets up a Flask web application for image processing using a pre-trained model.

It imports necessary libraries and functions for the application to work,
including Flask for web framework functionality, 
rendering HTML templates, and handling HTTP requests. It also imports 
functions from the 'model' module for image preprocessing and making predictions.

The application allows users to upload an image, preprocess it using the 
'preprocess_img' function, and predict a result using the 
'predict_result' function. The results are then displayed to the user.

Author: [Your Name]
Date: [Current Date]
"""

from flask import Flask, render_template, request
from model import preprocess_img, predict_result

# Instantiating flask app
app = Flask(__name__)


# Home route
@app.route("/")
def main():
    """
    Renders the main web page.

    This function is responsible for rendering the main web page, typically the homepage
    of a web application. It uses the 'render_template' function to display the 'index.html'
    template.

    Returns:
        str: The rendered HTML content of the 'index.html' page.
    """
    return render_template("index.html")


# Prediction route
@app.route('/prediction', methods=['POST'])
def predict_image_file():
    """
    Predicts the content of an uploaded image file and returns the result.

    This function expects a POST request with an image file, processes the image,
    and returns the prediction result.

    Returns:
        str: A prediction result or an error message if there's an issue with the file.
    """
    try:
        if request.method == 'POST':
            img = preprocess_img(request.files['file'].stream)
            pred = predict_result(img)
            # return render_template("result.html", predictions=str(pred))
            return "Successfull"
    except (FileNotFoundError, ValueError) as error_message:
        error = "File cannot be processed: " + str(error_message)
        # return render_template("result.html", err=error)
        return "Error"

    # If none of the conditions above are met, return something consistent.
    # You can replace this with an appropriate default response.
    return "Something went wrong!"


# Driver code
if __name__ == "__main__":
    app.run(port=9000, debug=True)
