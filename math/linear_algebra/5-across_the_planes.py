#!/usr/bin/env python3

def add_matrices2D(mat1, mat2):
    # Check if both matrices have the same number of rows
    if len(mat1) != len(mat2):
        return None
    
    # Check if each row has the same length
    for i in range(len(mat1)):
        if len(mat1[i]) != len(mat2[i]):
            return None
    
    # Return a new matrix with element-wise sums
    return [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[i]))] for i in range(len(mat1))]

# Test cases
if __name__ == "__main__":
    mat1 = [[1, 2], [3, 4]]
    mat2 = [[5, 6], [7, 8]]
    print(add_matrices2D(mat1, mat2))  # Output: [[6, 8], [10, 12]]
    print(mat1)  # Output: [[1, 2], [3, 4]]
    print(mat2)  # Output: [[5, 6], [7, 8]]
