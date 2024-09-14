#!/usr/bin/env python3

def mat_mul(mat1, mat2):
    """Performs matrix multiplication on two 2D matrices.
    
    Args:
        mat1: First matrix (list of lists).
        mat2: Second matrix (list of lists).
    
    Returns:
        A new matrix resulting from the multiplication of mat1 and mat2,
        or None if the matrices cannot be multiplied.
    """
    # Get the dimensions of mat1 and mat2
    rows_mat1 = len(mat1)
    cols_mat1 = len(mat1[0])
    rows_mat2 = len(mat2)
    cols_mat2 = len(mat2[0])
    
    # Check if multiplication is possible (columns of mat1 must match rows of mat2)
    if cols_mat1 != rows_mat2:
        return None
    
    # Initialize the result matrix with zeros
    result = [[0 for _ in range(cols_mat2)] for _ in range(rows_mat1)]
    
    # Perform matrix multiplication
    for i in range(rows_mat1):
        for j in range(cols_mat2):
            for k in range(cols_mat1):
                result[i][j] += mat1[i][k] * mat2[k][j]
    
    return result

# Test cases
if __name__ == "__main__":
    mat1 = [[1, 2],
            [3, 4],
            [5, 6]]
    
    mat2 = [[1, 2, 3, 4],
            [5, 6, 7, 8]]
    
    print(mat_mul(mat1, mat2))
