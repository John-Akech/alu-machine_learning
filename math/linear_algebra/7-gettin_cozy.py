#!/usr/bin/env python3

def cat_matrices2D(mat1, mat2, axis=0):
    """Concatenates two 2D matrices along a specific axis.
    
    Args:
        mat1: First matrix (list of lists).
        mat2: Second matrix (list of lists).
        axis: Axis along which to concatenate (default is 0).
    
    Returns:
        A new matrix representing the concatenation, or None if they cannot be concatenated.
    """
    # Check if the shapes of the matrices are compatible for concatenation
    if axis == 0:  # Concatenating along rows
        if len(mat1[0]) != len(mat2[0]):  # Number of columns must match
            return None
        return [row[:] for row in mat1] + [row[:] for row in mat2]
    elif axis == 1:  # Concatenating along columns
        if len(mat1) != len(mat2):  # Number of rows must match
            return None
        return [row1 + row2 for row1, row2 in zip(mat1, mat2)]
    else:
        return None

# Test cases
if __name__ == "__main__":
    mat1 = [[1, 2], [3, 4]]
    mat2 = [[5, 6]]
    mat3 = [[7], [8]]

    # Concatenating along axis 0 (rows)
    mat4 = cat_matrices2D(mat1, mat2)
    # Concatenating along axis 1 (columns)
    mat5 = cat_matrices2D(mat1, mat3, axis=1)

    print(mat4)  # Expected: [[1, 2], [3, 4], [5, 6]]
    print(mat5)  # Expected: [[1, 2, 7], [3, 4, 8]]

    # Testing modification of mat1 after concatenation
    mat1[0] = [9, 10]
    mat1[1].append(5)
    print(mat1)  # Expected: [[9, 10], [3, 4, 5]]
    print(mat4)  # mat4 should not change: [[1, 2], [3, 4], [5, 6]]
    print(mat5)  # mat5 should not change: [[1, 2, 7], [3, 4, 8]]
