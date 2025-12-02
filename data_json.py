# data_json.py
import json
import matplotlib.pyplot as plt

def visualize_earthquake(path="data/earthquake.json"):
    with open(path) as f:
        data = json.load(f)

    mags, lons, lats = [], [], []

    for quake in data["features"]:
        mags.append(quake["properties"]["mag"])
        lons.append(quake["geometry"]["coordinates"][0])
        lats.append(quake["geometry"]["coordinates"][1])

    plt.figure(figsize=(10, 6))
    plt.scatter(lons, lats, s=[m*5 for m in mags])
    plt.title("Earthquake Map")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.savefig("output_earthquake.png")  # Lưu ra file
    print("Saved Earthquake plot as output_earthquake.png")
