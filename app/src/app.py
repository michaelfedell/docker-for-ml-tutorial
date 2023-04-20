from pathlib import Path
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import uvicorn

# Load the Iris dataset and trained classifier
artifacts = Path() / "artifacts"
iris = joblib.load(artifacts / "iris.joblib")
clf = joblib.load(artifacts / "iris_classifier.joblib")


# Define the input data schema
class InputData(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


# Create the FastAPI app
app = FastAPI()


@app.get("/")
def root():
    return {"app": "iris-inference", "version": "v1"}


# Define the inference route
@app.post("/predict")
def predict(data: InputData):
    # Convert the input data to a NumPy array
    input_data = np.array(
        [data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]
    ).reshape(1, -1)

    # Make a prediction with the trained classifier
    prediction = clf.predict(input_data)[0]

    # Get the predicted class label and name
    class_label = int(prediction)
    class_name = str(iris.target_names[class_label])

    # Return the prediction as a JSON response
    return {"class_label": class_label, "class_name": class_name}


def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("src.app:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    start()