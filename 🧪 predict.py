import pickle
import numpy as np

with open("xgb_model.pkl", "rb") as file:
    model = pickle.load(file)

sample = np.array([[5.59, 3.35, 0, 1, 50000, 0, 8]])

prediction = model.predict(sample)

print("Predicted Selling Price:", prediction[0])