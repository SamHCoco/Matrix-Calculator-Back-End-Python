#  Matrix Calculator: Overview of Capabilities

This source code provides a command-line matrix calculator written in Python capable of performing
the following calculations with matrices:

* **ADDITION:** Two matrices, **A** and **B**, can be added once both matrices are created as objects and their values inputted by the user.

```Python
# Creates matrices (will ask for user input)
  matrix_a = Matrix(3, 3, "A")
  matrix_b = Matrix(3, 3, "B")

# Adding A + B
  matrix_a.add(matrix_b)
```

* **MULTIPLCATION:** Using the **Naïve Matrix Multiplication** algorithm of summing products. As such, this calculator is **not recommended for large matrices**. Any appropriately sized matrices can be multiplied together.

```Python
# Creates matrices (will ask for user input)
  matrix_a = Matrix(4, 3, "A")
  matrix_b = Matrix(3, 2, "B")

# Multiplying A by B (A*B)
  matrix_a.multiply(matrix_b)
```

* **SCALAR MULTIPLCATION:** Any matrix, **B**, may be multiplied by a scalar value, *a*, to return *a* * **B**.

```Python
  matrixB = Matrix(3, 4, "B")
  # Scalar multiplies matrix B by scalar value 'a'.
  matrixB.scalar_muliply(a)
```

* **DETERMINANT:** Determinants of **2x2** and **3x3 matrices** can be calculated.

```Python
  matrix_a = Matrix(3, 3, "A")
# Calculates Determinant of A
  matrix_a.find_determinant()
```

* **DOT PRODUCT:** The dot product of two vectors may be calculated.

```Python
  vector_1 = [3.24, 6.45, 6]
  vector_2 = [54.6, 23.5, -4.5]
# Calculates the dot product
  Matrix.dot_product(vector_1, vector_2)

```

## Other Useful Functionality:

* The minor matrices for calculating cofactors may be extracted from any 3x3 matrix.

```Python
  matrix_a = Matrix(3, 3, "A")
  # Extract cofactor matrices
  minor_matrices = matrix_a.extract_2x2_minor_matrices()
```

The returned result will be a list. Each of the elements of the list is a row of a minor matrix. The **first two elements** are the **1st minor matrix**, the **third and fourth elements** are the **2nd minor matrix** and the **fifth and sixth elements** are the **3rd minor matrix**.

## Precision of Results:
All results are given to 3 decimal places, where necessary.
