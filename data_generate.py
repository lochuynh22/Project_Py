# data_generate.py
import matplotlib.pyplot as plt
from random import choice

class RandomWalk:
    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_step = choice([1, -1, 2, -2, 0])
            y_step = choice([1, -1, 2, -2, 0])

            if x_step == 0 and y_step == 0:
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

def visualize_random_walk():
    rw = RandomWalk(5000)
    rw.fill_walk()

    plt.figure(figsize=(10, 6))
    plt.scatter(rw.x_values, rw.y_values, s=5)
    plt.title("Random Walk Visualization")
    plt.savefig("output_random_walk.png")  # Lưu ra file
    print("Saved Random Walk plot as output_random_walk.png")