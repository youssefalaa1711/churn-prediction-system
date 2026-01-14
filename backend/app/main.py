from fastapi import FastAPI
from backend.app.predict import predict_churn
from backend.app.schemas import CustomerInput

app = FastAPI(title="Customer Churn Prediction API")

@app.post("/predict")
def predict(data: CustomerInput):
    return predict_churn(data.model_dump())
