# Advanced Linear Algebra: Learning Objectives

## Overview
At the end of this project, I expect to be able to explain the following concepts in linear algebra without the help of Google.

## Learning Objectives

### 1. Determinant
- **Definition**: I understand that the determinant is a scalar value derived from the elements of a square matrix. It provides important information about the matrix, including whether it is invertible.
- **Calculation**:
  - For a 2x2 matrix \(\begin{bmatrix} a & b \\ c & d \end{bmatrix}\), I calculate the determinant as:
    \[
    \text{det}(A) = ad - bc
    \]
  - For a 3x3 matrix \(\begin{bmatrix} a & b & c \\ d & e & f \\ g & h & i \end{bmatrix}\), I calculate the determinant as:
    \[
    \text{det}(A) = a(ei - fh) - b(di - fg) + c(dh - eg)
    \]

### 2. Minor, Cofactor, and Adjugate
- **Minor**: I recognize that the minor of an element in a matrix is the determinant of the submatrix formed by deleting the row and column of that element.
- **Cofactor**: I calculate the cofactor of an element as:
  \[
  C_{ij} = (-1)^{i+j} \cdot M_{ij}
  \]
  where \(M_{ij}\) is the minor of the element at position \((i, j)\).
- **Adjugate**: I know that the adjugate of a matrix is the transpose of its cofactor matrix, which I can use to calculate the inverse of a matrix.

### 3. Inverse
- **Definition**: I understand that the inverse of a matrix \(A\) is another matrix \(A^{-1}\) such that:
  \[
  A \cdot A^{-1} = I
  \]
  where \(I\) is the identity matrix.
- **Calculation**:
  - For a 2x2 matrix:
    \[
    A^{-1} = \frac{1}{\text{det}(A)} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}
    \]
  - For larger matrices, I calculate the inverse using the formula:
    \[
    A^{-1} = \frac{1}{\text{det}(A)} \text{adj}(A)
    \]

### 4. Eigenvalues and Eigenvectors
- **Definition**: I know that eigenvalues are scalars associated with a matrix that indicate how much the corresponding eigenvectors are stretched or compressed during the transformation represented by the matrix.
- **Calculation**:
  - To find eigenvalues \(\lambda\), I solve the characteristic polynomial:
    \[
    \text{det}(A - \lambda I) = 0
    \]
  - Once I find the eigenvalues, I substitute them back into \(A - \lambda I\) to solve for the eigenvectors.

### 5. Definiteness of a Matrix
- **Definition**: I understand that the definiteness of a matrix indicates whether it is positive definite, negative definite, indefinite, or positive semi-definite, based on the sign of its eigenvalues or leading principal minors.
- **Determination**:
  - I compute the leading principal minors and analyze their signs:
    - A matrix is **positive definite** if all leading principal minors are positive.
    - A matrix is **negative definite** if the leading principal minors alternate in sign, starting with negative.
    - A matrix is **indefinite** if there are both positive and negative leading principal minors.
    - A matrix is **positive semi-definite** if all leading principal minors are non-negative, with at least one minor being zero.

## Conclusion
By mastering these concepts, I will have a strong foundation in advanced linear algebra that will enable me to tackle complex problems and explain key ideas clearly.
