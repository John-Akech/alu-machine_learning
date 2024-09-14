#!/usr/bin/env python3

def add_matrices(mat1, mat2):
    # Check if the shapes of the matrices are the same
    if not isinstance(mat1, list) or not isinstance(mat2, list):
        return None
    
    # Helper function to check the shape of the matrix
    def check_shape(matrix):
        shape = []
        while isinstance(matrix, list):
            shape.append(len(matrix))
            matrix = matrix[0] if matrix else []
        return shape
    
    shape1 = check_shape(mat1)
    shape2 = check_shape(mat2)
    
    if shape1 != shape2:
        return None
    
    # Recursive function to add matrices
    def add_recursive(m1, m2):
        if isinstance(m1[0], list):
            return [add_recursive(a, b) for a, b in zip(m1, m2)]
        else:
            return [x + y for x, y in zip(m1, m2)]
    
    return add_recursive(mat1, mat2)
