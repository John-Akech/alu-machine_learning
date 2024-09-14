#!/usr/bin/env python3
"""
This script uses Matplotlib to plot a line graph of the function y = x^3.
It demonstrates basic plotting with a solid red line and custom axis labels.
"""

import numpy as np
import matplotlib.pyplot as plt

# Generate y values
y = np.arange(0, 11) ** 3

# Plot y as a solid red line
plt.plot(np.arange(0, 11), y, 'r-')  # 'r-' for solid red line

# Set axis labels and title
plt.xlim(0, 10)  # Set x-axis range from 0 to 10
plt.xlabel("X-axis")
plt.ylabel("Y-axis (X^3)")
plt.title("Line Graph of Y = X^3")

# Display the plot
plt.show()
