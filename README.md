#  Matrix Calculator: Overview of Capabilities

This source code provides a command-line matrix calculator written in Python capable of performing
the following calculations with matrices:

* **ADDITION:** Two matrices, **A** and **B**, can be added once both matrices are created as objects and their values inputted by the user.

```Python
# Creates matrices (will ask for user input)
  matrixA = Matrix(3, 3, "A")
  matrixB = Matrix(3, 3, "B")

# Adding A + B
matrixA.add(matrixB)
```

* **MULTIPLCATION:** Using the **Naïve Matrix Multiplication** algorithm of summing products. As such, this calculator is **not recommended for large matrices**. Any appropriately sized matrices can be multiplied together.

```Python
# Creates matrices (will ask for user input)
  matrixA = Matrix(4, 3, "A")
  matrixB = Matrix(3, 2, "B")

# Multiplying A by B (A*B)
  matrixA.multiply(matrixB)
```

* **SCALAR MULTIPLCATION:** Any matrix, **B**, may be multiplied by a scalar value, *a*, to return *a* * **B**.

```Python
  MatrixB = Matrix(3, 4, "B")
  # Scalar multiplies matrix B by scalar value 'a'.
  MatrixB.scalar_muliply(a)
```

* **DETERMINANT:** Determinants of **2x2** and **3x3 matrices** can be calculated.

```Python
  MatrixA = Matrix(3, 3, "A")
# Calculates Determinant of A
  MatrixA.find_determinant()
```

* **DOT PRODUCT:** The dot product of two vectors may be calculated.

```Python
  vector_1 = Matrix(1, 4, "Vector_1")
  vector_2 = Matrix(1, 4, "Vector_2")
# Calculates the dot product
  Matrix.dot_product(vector_1, vector_2)

```

## Other Useful Functionality:

* The matrices for calculating a matrix cofactor may be extracted and returned

## Precision of Results:
All results are given to 3 decimal places
