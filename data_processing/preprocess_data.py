import json

def preprocess_data(filename):
    with open(filename, "r") as file:
        data = json.load(file)
    # Add preprocessing steps here (e.g., normalization, filtering)
    print(f"Data preprocessed for file {filename}")
