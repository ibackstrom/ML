import pickle

with open("table", "rb") as file:
    ct = pickle.load(file)
print(ct)

