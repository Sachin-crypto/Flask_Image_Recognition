
"""Flask application for handwritten digit recognition."""

from flask import Flask, render_template, request
from model import preprocess_img, predict_result

app = Flask(__name__)


@app.route("/")
def main():
    """Display the application's homepage."""
    return render_template("index.html")


@app.route("/prediction", methods=["POST"])
def predict_image_file():
    """Process an uploaded image and display the predicted digit."""
    uploaded_file = request.files.get("file")

    if uploaded_file is None or uploaded_file.filename == "":
        return render_template(
            "result.html",
            err="Please select an image file."
        )

    try:
        img = preprocess_img(uploaded_file.stream)
        pred = predict_result(img)
        return render_template("result.html", predictions=str(pred))
    except (OSError, ValueError):
        app.logger.exception("Failed to process uploaded image.")
        return render_template(
            "result.html",
            err="File cannot be processed."
        )


if __name__ == "__main__":
    app.run(port=9000, debug=True)
def this_function_is_not_used():
    """Demonstrate a function with a docstring."""
    print("Temporary Pylint demonstration")
