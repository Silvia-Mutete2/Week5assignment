import os
from joblib import dump
from sklearn.linear_model import LogisticRegression


def train_model(X, y, model_path: str = 'models/model.joblib'):
    """Train a simple classifier and save it to `model_path`.

    Returns the trained model object.
    """
    model = LogisticRegression(max_iter=200)
    model.fit(X, y)
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    dump(model, model_path)
    return model
