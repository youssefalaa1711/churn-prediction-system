import pickle
import json

with open("notebooks/model.pkl", "rb") as f:
    model = pickle.load(f)

with open("notebooks/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("notebooks/feature_columns.json", "r") as f:
    feature_columns = json.load(f)
