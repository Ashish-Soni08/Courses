import pickle

pkl_filename = "D:/Github/DPS_Challenge/dps_model.pkl"

# Load model
with open(pkl_filename, "rb") as file:
  pickle.load(file)