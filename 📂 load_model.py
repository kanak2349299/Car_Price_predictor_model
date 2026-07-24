import pickle

with open("xgb_model.pkl", "rb") as file:
    model = pickle.load(file)

print("✅ Model loaded successfully!")