# Linear Algebra Project

## Overview

This project provides Python functions for basic linear algebra operations, such as matrix addition, concatenation, and slicing. It is designed to help users understand fundamental concepts in linear algebra and practice using these concepts programmatically.

## Learning Objectives

By the end of this project, you should be able to explain:

- **Vector**: A one-dimensional array of numbers.
- **Matrix**: A two-dimensional array of numbers arranged in rows and columns.
- **Transpose**: An operation that flips a matrix over its diagonal, swapping rows and columns.
- **Shape**: The dimensions of a matrix, represented as a tuple indicating the number of rows and columns.
- **Axis**: A dimension along which operations (e.g., concatenation, slicing) are performed in arrays.
- **Slice**: A subset of an array or matrix defined by specifying a range of indices.
- **Slicing a Vector/Matrix**: Extracting portions of a vector or matrix using slicing operations.
- **Element-Wise Operations**: Operations performed on corresponding elements of vectors or matrices (e.g., addition, multiplication).
- **Concatenate Vectors/Matrices**: Combining vectors or matrices along a specified axis.
- **Dot Product**: A scalar product of two vectors, calculated as the sum of the products of their corresponding elements.
- **Matrix Multiplication**: An operation that produces a matrix by multiplying rows of the first matrix with columns of the second matrix.
- **Numpy**: A Python library used for numerical operations on arrays and matrices.
- **Parallelization**: The process of executing multiple operations simultaneously to improve performance and efficiency.
- **Broadcasting**: A mechanism that allows numpy to perform element-wise operations on arrays of different shapes by automatically expanding their dimensions.

## Installation

Ensure you have Python 3.5 installed. No additional packages are required.

## Usage

1. **Matrix Addition:**

   Function: `add_matrices(mat1, mat2)`

   Adds two matrices of the same shape. Returns a new matrix or `None` if the shapes do not match.

2. **Matrix Concatenation:**

   Function: `cat_matrices(mat1, mat2, axis=0)`

   Concatenates two matrices along the specified axis. Returns a new matrix or `None` if concatenation is not possible.

3. **Matrix Slicing:**

   Function: `np_slice(matrix, axes={})`

   Slices a matrix along specified axes. The `axes` parameter is a dictionary where keys represent axes and values are slices.


Contribution

Feel free to submit issues and pull requests to improve the project.
