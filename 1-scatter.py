#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x, y = np.random.multivariate_normal(mean, cov, 2000).T
y += 180

# Plot x ↦ y as a scatter plot
plt.scatter(x, y, color='magenta')  # Scatter plot with magenta points
plt.xlabel("Height (in)")           # Label for x-axis
plt.ylabel("Weight (lbs)")          # Label for y-axis
plt.title("Men's Height vs Weight") # Title of the plot
plt.show()
