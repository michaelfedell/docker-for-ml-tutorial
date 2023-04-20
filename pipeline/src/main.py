from pathlib import Path

import joblib
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

artifacts = Path() / "artifacts"
artifacts.mkdir(exist_ok=True)
print(artifacts.absolute())


def main():
    """Run the pipeline to produce a classifier model for the Iris dataset"""
    # Load the Iris dataset
    iris = load_iris(return_X_y=False)

    # Split the dataset into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42
    )

    # Create a decision tree classifier
    clf = DecisionTreeClassifier()

    # Train the classifier on the training set
    clf.fit(X_train, y_train)

    # Evaluate the classifier on the test set
    score = clf.score(X_test, y_test)
    print(f"Classifier accuracy: {score:.2f}")

    # Save the data and model to the file system
    joblib.dump(iris, artifacts / "iris.joblib")
    joblib.dump(clf, artifacts / "iris_classifier.joblib")


if __name__ == "__main__":
    main()
