def matrix_transpose(matrix):
    # Transpose the matrix using list comprehension and the zip function
    return [list(row) for row in zip(*matrix)]

# Test cases
if __name__ == "__main__":
    mat1 = [[1, 2], [3, 4]]
    print("Original matrix:")
    print(mat1)
    print("Transposed matrix:")
    print(matrix_transpose(mat1))

    mat2 = [[1, 2, 3, 4, 5], 
            [6, 7, 8, 9, 10], 
            [11, 12, 13, 14, 15], 
            [16, 17, 18, 19, 20], 
            [21, 22, 23, 24, 25], 
            [26, 27, 28, 29, 30]]
    print("Original matrix:")
    print(mat2)
    print("Transposed matrix:")
    print(matrix_transpose(mat2))  # Output: Transposed version of mat2
