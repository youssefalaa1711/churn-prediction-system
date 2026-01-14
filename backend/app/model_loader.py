from pathlib import Path
import pickle
import json

# backend/app/model_loader.py
BASE_DIR = Path(__file__).resolve().parents[2]  # /app
ARTIFACTS_DIR = BASE_DIR / "artifacts"

def load_artifacts():
    try:
        with open(ARTIFACTS_DIR / "model.pkl", "rb") as f:
            model = pickle.load(f)

        with open(ARTIFACTS_DIR / "scaler.pkl", "rb") as f:
            scaler = pickle.load(f)

        with open(ARTIFACTS_DIR / "feature_columns.json", "r") as f:
            feature_columns = json.load(f)

        return model, scaler, feature_columns

    except Exception as e:
        raise RuntimeError(f"Failed to load model artifacts: {e}")
