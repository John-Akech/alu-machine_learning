#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 21001, 1000)  # Adjusted upper limit to include 20000
r = np.log(0.5)
t1 = 5730
t2 = 1600
y1 = np.exp((r / t1) * x)
y2 = np.exp((r / t2) * x)

# Plot x ↦ y1 and x ↦ y2 as line graphs
plt.plot(x, y1, 'r--', label='C-14')  # Dashed red line for C-14
plt.plot(x, y2, 'g-', label='Ra-226')  # Solid green line for Ra-226

plt.xlim(0, 20000)   # Set x-axis range from 0 to 20000
plt.ylim(0, 1)       # Set y-axis range from 0 to 1
plt.xlabel("Time (years)")            # Label for x-axis
plt.ylabel("Fraction Remaining")      # Label for y-axis
plt.title("Exponential Decay of Radioactive Elements") # Title of the plot
plt.legend(loc='upper right')         # Place legend in the upper right corner

plt.show()
