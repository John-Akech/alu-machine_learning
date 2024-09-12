#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

# Plot histogram of student grades
plt.hist(student_grades, bins=np.arange(0, 101, 10), edgecolor='black')  # Bins every 10 units with black outlines
plt.xlabel("Grades")                    # Label for x-axis
plt.ylabel("Number of Students")        # Label for y-axis
plt.title("Project A")                  # Title of the plot
plt.show()
