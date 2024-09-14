#!/usr/bin/env python3
import numpy as np

# Initialize the matrix as per the requirement
matrix = np.array([[1, 2, 3, 4, 5, 6], 
                   [7, 8, 9, 10, 11, 12], 
                   [13, 14, 15, 16, 17, 18], 
                   [19, 20, 21, 22, 23, 24]])

# Slice operations
mat1 = matrix[1:3]  # Middle two rows of the matrix
mat2 = matrix[:, 2:4]  # Middle two columns of the matrix
mat3 = matrix[1:, 3:]  # Bottom-right 3x3 matrix

# Print the results
print("The middle two rows of the matrix are:\n{}".format(mat1))
print("The middle two columns of the matrix are:\n{}".format(mat2))
print("The bottom-right, square, 3x3 matrix is:\n{}".format(mat3))
