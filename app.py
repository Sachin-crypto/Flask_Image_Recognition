"""
Flask application for image prediction.

This module provides:
- Home page rendering.
- Image upload and prediction route.
- Integration with model preprocessing and prediction functions.
"""

# Importing required libs
from flask import Flask, render_template, request
from model import preprocess_img, predict_result

# Instantiating flask app
app = Flask(__name__)


# Home route
@app.route("/")
def main():
    """
    Render the home page.

    Returns:
        str: Rendered HTML template for the home page.
    """
    return render_template("index.html")


# Prediction route
@app.route('/prediction', methods=['POST'])
def predict_image_file():
    """
    Process an uploaded image and return prediction results.

    - Reads the uploaded image from the request.
    - Preprocesses the image using the model's preprocess function.
    - Predicts results using the model's predict function.
    - Returns rendered result page with predictions or error message.

    Returns:
        str: Rendered HTML template with prediction or error message.
    """
    try:
        if request.method == 'POST':
            img = preprocess_img(request.files['file'].stream)
            pred = predict_result(img)
            return render_template("result.html", predictions=str(pred))

    except Exception:
        error = "File cannot be processed."
        return render_template("result.html", err=error)

    return render_template("index.html")


# Driver code

if __name__ == "__main__":
    # Run the Flask application on port 9000 with debug mode enabled.
    app.run(port=9000, debug=True)
