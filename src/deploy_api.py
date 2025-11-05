from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import os
import pandas as pd


class Features(BaseModel):
    feature1: float
    feature2: float
    feature3: float


app = FastAPI()
MODEL_PATH = os.environ.get('MODEL_PATH', 'models/model.joblib')
model = None


@app.on_event('startup')
def load_model():
    global model
    model = joblib.load(MODEL_PATH)


@app.post('/predict')
def predict(feat: Features):
    df = pd.DataFrame([feat.dict()])
    # In this starter example we assume the model accepts the raw features as-is
    pred = int(model.predict(df)[0])
    return {'prediction': pred}
