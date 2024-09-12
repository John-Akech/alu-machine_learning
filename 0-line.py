#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y = np.arange(0, 11) ** 3

# Plot y as a solid red line
plt.plot(np.arange(0, 11), y, 'r-')  # 'r-' for solid red line
plt.xlim(0, 10)  # Set x-axis range from 0 to 10
plt.xlabel("X-axis")
plt.ylabel("Y-axis (X^3)")
plt.title("Line Graph of Y = X^3")
plt.grid(True)
plt.show()
