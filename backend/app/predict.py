import pandas as pd

from backend.app.model_loader import model, scaler, feature_columns

# Numerical columns used during training
NUM_COLS = ["tenure", "MonthlyCharges", "TotalCharges"]


def predict_churn(input_data: dict):
    """
    Takes raw customer input data and returns churn probability and prediction.
    """

    # 1. Convert raw input dictionary into a DataFrame
    df = pd.DataFrame([input_data])

    # 2. One-hot encode categorical features
    df = pd.get_dummies(df)

    # 3. Align input features with training features
    df = df.reindex(columns=feature_columns, fill_value=0)

    # 4. Scale numerical features
    df[NUM_COLS] = scaler.transform(df[NUM_COLS])

    # 5. Make prediction
    churn_probability = model.predict_proba(df)[0][1]
    churn_prediction = int(churn_probability >= 0.5)

    return {
        "churn_probability": churn_probability,
        "churn_prediction": churn_prediction
    }
