from sklearn.metrics import accuracy_score, classification_report


def evaluate(model, X_test, y_test):
    """Evaluate model and return metrics."""
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    report = classification_report(y_test, preds)
    return {"accuracy": acc, "report": report}
