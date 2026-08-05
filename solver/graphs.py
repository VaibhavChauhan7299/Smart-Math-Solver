import numpy as np
import matplotlib.pyplot as plt


def plot_function():

    x = np.linspace(-10, 10, 400)

    y = x**2

    plt.plot(x, y)

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("y = x²")

    plt.grid(True)
    plt.show()