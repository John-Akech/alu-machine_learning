#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 28651, 5730)
r = np.log(0.5)
t = 5730
y = np.exp((r / t) * x)

# Plot x ↦ y as a line graph
plt.plot(x, y, 'b-')  # Line plot with a blue line
plt.yscale('log')    # Set y-axis to logarithmic scale
plt.xlim(0, 28650)   # Set x-axis range from 0 to 28650
plt.xlabel("Time (years)")            # Label for x-axis
plt.ylabel("Fraction Remaining")      # Label for y-axis
plt.title("Exponential Decay of C-14") # Title of the plot
plt.grid(True, which="both", ls="--")  # Add gridlines for both major and minor ticks
plt.show()
