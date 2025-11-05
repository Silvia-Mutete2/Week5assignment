import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    """Load CSV data into a pandas DataFrame."""
    return pd.read_csv(path)


def preprocess(df: pd.DataFrame):
    """Basic preprocessing: drop NA and split features/target.

    Returns:
        X (DataFrame): feature matrix
        y (Series): target vector
    """
    df = df.dropna()
    if 'target' not in df.columns:
        raise ValueError("Input DataFrame must contain a 'target' column")
    X = df.drop('target', axis=1)
    y = df['target']
    return X, y
