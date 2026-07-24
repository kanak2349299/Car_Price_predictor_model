import pickle

with open("xgb_model.pkl", "wb") as file:
    pickle.dump(xgb, file)

print("✅ XGBoost model saved successfully!")