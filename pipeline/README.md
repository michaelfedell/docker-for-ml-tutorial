# Iris Pipeline

This is a simple machine learning pipeline that trains a classifier on the [Iris dataset](https://archive.ics.uci.edu/ml/datasets/iris) using `scikit-learn`, and saves the trained model to disk as a `joblib` file.

## Usage

To use this pipeline, you can run the `train_classifier.py` script, which will train the classifier and save the model files to disk.

```bash
python train_classifier.py
```

By default, the script uses the iris.csv dataset file in the same directory as input data. You can modify this file to use your own data. The script outputs two joblib files, `model.joblib` and `iris.joblib`, which contain the trained classifier and preprocessed data respectively.

## Docker

To run the pipeline in a Docker container, you can use the following commands:

```bash
docker build -t iris-pipeline .
docker run -d --name iris-pipeline iris-pipeline
```

This will build a Docker image for the pipeline, and then run a container based on that image. The container will train the classifier and save the model files to disk during startup.
