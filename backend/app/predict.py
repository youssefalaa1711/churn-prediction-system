import pandas as pd
from backend.app.model_loader import load_artifacts

# Load artifacts ONCE
model, scaler, feature_columns = load_artifacts()

# Numerical columns used during training
NUM_COLS = ["tenure", "MonthlyCharges", "TotalCharges"]


def predict_churn(input_data: dict):
    """
    Takes raw customer input data and returns churn probability and prediction.
    """

    #  Convert input dictionary to DataFrame
    df = pd.DataFrame([input_data])

    #  One-hot encode categorical features
    df = pd.get_dummies(df)

    #  Align input features with training features
    df = df.reindex(columns=feature_columns, fill_value=0)

    #  Scale numerical features
    df[NUM_COLS] = scaler.transform(df[NUM_COLS])

    #  Predict
    churn_probability = model.predict_proba(df)[0][1]
    churn_prediction = int(churn_probability >= 0.5)

    return {
        "churn_probability": churn_probability,
        "churn_prediction": churn_prediction
    }
