# data_csv.py
import csv
import matplotlib.pyplot as plt
from datetime import datetime

def visualize_csv_weather(path="data/weather.csv"):
    dates, highs = [], []

    with open(path) as f:
        reader = csv.reader(f)
        header = next(reader)

        for row in reader:
            date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])

            dates.append(date)
            highs.append(high)

    plt.figure(figsize=(10, 5))
    plt.plot(dates, highs)
    plt.title("Daily High Temperatures")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.savefig("output_weather.png")  # Lưu ra file
    print("Saved Weather plot as output_weather.png")
