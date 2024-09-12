#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

# Data preparation
y0 = np.arange(0, 11) ** 3

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

x3 = np.arange(0, 21001, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

# Create a figure and set of subplots
fig, axs = plt.subplots(3, 2, figsize=(12, 15), gridspec_kw={'height_ratios': [1, 1, 2]})
fig.suptitle('All in One', fontsize='x-small')

# Plot 1: Line graph for y0
axs[0, 0].plot(np.arange(0, 11), y0, 'r-')
axs[0, 0].set_xlim(0, 10)
axs[0, 0].set_xlabel('X-axis', fontsize='x-small')
axs[0, 0].set_ylabel('Y-axis (X^3)', fontsize='x-small')
axs[0, 0].set_title('Line Graph of Y = X^3', fontsize='x-small')

# Plot 2: Scatter plot for x1, y1
axs[0, 1].scatter(x1, y1, color='magenta')
axs[0, 1].set_xlabel('Height (in)', fontsize='x-small')
axs[0, 1].set_ylabel('Weight (lbs)', fontsize='x-small')
axs[0, 1].set_title("Men's Height vs Weight", fontsize='x-small')
axs[0, 1].grid(True)

# Plot 3: Line graph with logarithmic y-axis
axs[1, 0].plot(x2, y2, 'b-')
axs[1, 0].set_yscale('log')
axs[1, 0].set_xlim(0, 28650)
axs[1, 0].set_xlabel('Time (years)', fontsize='x-small')
axs[1, 0].set_ylabel('Fraction Remaining', fontsize='x-small')
axs[1, 0].set_title('Exponential Decay of C-14', fontsize='x-small')

# Plot 4: Line graph for y31 and y32
axs[1, 1].plot(x3, y31, 'r--', label='C-14')
axs[1, 1].plot(x3, y32, 'g-', label='Ra-226')
axs[1, 1].set_xlim(0, 20000)
axs[1, 1].set_ylim(0, 1)
axs[1, 1].set_xlabel('Time (years)', fontsize='x-small')
axs[1, 1].set_ylabel('Fraction Remaining', fontsize='x-small')
axs[1, 1].set_title('Exponential Decay of Radioactive Elements', fontsize='x-small')
axs[1, 1].legend(loc='upper right')

# Plot 5: Histogram of student grades
axs[2, 0].hist(student_grades, bins=np.arange(0, 101, 10), edgecolor='black')
axs[2, 0].set_xticks(np.arange(0, 101, 10))  # Set x-axis ticks for Grades
axs[2, 0].set_yticks(np.arange(0, 31, 10))   # Set y-axis ticks for Number of Students
axs[2, 0].set_xlabel('Grades', fontsize='x-small')
axs[2, 0].set_ylabel('Number of Students', fontsize='x-small')
axs[2, 0].set_title('Project A', fontsize='x-small')

# Hide the empty subplot
axs[2, 1].axis('off')

# Adjust layout
plt.tight_layout(rect=[0, 0, 1, 0.97])  # Adjust to make room for suptitle
plt.show()
