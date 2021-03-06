class Matrix:
    """ Defines a matrix and its operations (Add, multiply etc), with all results to 3 d.p.

    Attributes
    ----------
    rows (int) -- number rows in the matrix
    columns (int)-- number of columns in the matrix
    determinant (float)-- matrix determinant
    name (string)-- name of matrix
    matrix (list) -- contains matrix elements

    Methods
    -------
    print_matrix() - Prints matrix.

    add(m) - Adds m to matrix.

    scalar_multiply(a) - Multiplies matrix by scalar value a.

     multiply(m) - Multiplies matrix with matrix m.

     dot_product(v1, v2) - Calculates the dot product of two vectors.

     find_matrix_size() - Returns number of rows and columns in matrix

     find_determinant() - Returns determinant of matrix

     extract_2x2_minor_matrices() - Returns the minor matrices needed to calculate 3x3 matrix cofactors
    """

    def __init__(self, rows, columns, name, testing=False):
        """Create matrix instance.

       Args:
       rows (int) -- matrix rows
       columns (int)-- matrix columns
       name (string) -- matrix name
       testing (Boolean) -- For unit testing. Remove later.
        """
        self.rows = rows
        self.columns = columns
        self.determinant = None
        self.name = name
        self.matrix = []
        if not testing:
            self._create_matrix()
            self.print_matrix()

    def _create_matrix(self):
        """Input matrix values."""
        for i in range(0, self.rows):
            self.matrix.append([])
        print("Enter the elements of matrix " + self.name + " by row:")
        for i in range(0, self.rows):
            for j in range(0, self.columns):
                self.matrix[i].append(float(input()))

    def print_matrix(self):
        """Prints matrix object."""
        for i in range(0, self.rows):
            for j in range(0, self.columns):
                print("{:<3}".format(self.matrix[i][j]), end=' ')
            print("")
        print("*" * 200)  # star line to improve output readability

    def add(self, x):
        """Add another matrix, x, to the matrix.

        Args:
        x (list) -- a matrix of size NxN (N >= 1)
           
        Return: added matrices
        """
        if x.rows == self.rows and x.columns == self.columns:
            # performs matrix addition calculation
            for i in range(0, x.rows):
                for j in range(0, self.columns):
                    self.matrix[i][j] += x.matrix[i][j]
            print("RESULT OF ADDITION: " + x.name + " + " + self.name)
            self.print_matrix()
        else:
            print("Matrix " + x.name + " and " + self.name + " must be the same size")
        return self.matrix

    def scalar_multiply(self, scalar):
        """Multiply matrix by scalar and print result.

        Args:
        scalar (float/int) -- the value that will multiply the matrix
            
        Returns: scalar multiplied matrix
        """
        # performs scalar multiplication calculation
        for i in range(0, self.rows):
            for j in range(0, self.columns):
                self.matrix[i][j] = scalar * self.matrix[i][j]
        print("RESULT OF SCALAR MULTIPLICATION: {} * {}".format(scalar, self.name))
        self.print_matrix()
        return self.matrix

    def multiply(self, matrix):
        """Multiply matrix by another matrix A*B where B = matrix parameter.
        Args:
        matrix (list) -- the matrix that will multiply the user's matrix
            
        Return: multiplied matrices
        """
        result = []
        result_matrix = []
        column_vector = []
        # checks matrices have correct size
        if self.columns == matrix.rows:
            # calculates dot products of self.matrix rows and 'matrix' (argument) columns.
            for row_vector in self.matrix:
                i = 0
                while i < matrix.columns:
                    for row in matrix.matrix:
                        column_vector.append(row[i])
                    result.append(Matrix.dot_product(row_vector, column_vector))
                    column_vector.clear()
                    i += 1
            # takes result values and puts them into matrix format
            for i in range(0, self.rows):
                result_matrix.append(result[i * matrix.columns: (i + 1) * matrix.columns])
            # displays final result to the user
            print("RESULT OF MATRIX MULTIPLICATION : {} * {}".format(self.name, matrix.name))
            original_matrix = self.matrix
            self.matrix = result_matrix
            self.print_matrix()
            self.matrix = original_matrix
            return result_matrix
        else:
            print("MULTIPLY ERROR: Matrices do not have correct dimensions for multiplication")

    @staticmethod
    def dot_product(vector_1, vector_2):
        """Calculate dot product of two vectors.

        Args:
        vector_1 (list) -- first vector of dot product
        vector_2 (list) -- second vector of dot product

        Return: dot product to 3 d.p, or -1 if vectors not same size
        """
        result = 0
        if len(vector_1) == len(vector_2):
            for i in range(0, len(vector_1)):
                result += vector_1[i] * vector_2[i]
            return round(result, 3)
        else:
            print("Error: vectors must be the same length")
            return -1

    def find_matrix_size(self):
        """Determines whether matrix is 2x2 or 3x3.

        Return: 2 if matrix 2x2, 3 if matrix 3x3 or -1 if neither
        """
        if self.rows == 2 and self.columns == 2:
            return 2
        elif self.rows == 3 and self.columns == 3:
            return 3
        else:
            return -1

    def find_determinant(self):
        """Calculate matrix determinant.
        
        Return: determinant, rounded to 3 d.p
        """
        if self.find_matrix_size() == 2:
            self.determinant = self._calculate_2x2_determinant()
            print("Matrix {} Determinant = {:.3f}".format(self.name, self.determinant))
        elif self.find_matrix_size() == 3:
            self._calculate_3x3_determinant()
            print("Matrix {} Determinant = {:.3f}".format(self.name, self.determinant))
        return round(self.determinant, 3)

    def _calculate_2x2_determinant(self):
        """Calculate 2x2 matrix determinant.
        
        Return: determinant of 2x2 matrix (not rounded to 3 d.p)
        """
        return (self.matrix[0][0] * self.matrix[1][1]) - (self.matrix[1][0] * self.matrix[0][1])

    def _calculate_3x3_determinant(self):
        """Calculate 3x3 matrix determinant.
        
        Return: determinant of 3x3 matrix (not rounded to 3 d.p)
        """
        first_row = self.matrix[0]
        cofactor_matrices = self.extract_2x2_minor_matrices()
        print("cofactor matrices: {}".format(cofactor_matrices))
        original_matrix = self.matrix
        self.matrix = cofactor_matrices
        self.determinant = 0
        for i in range(0, 3):
            minor = self._calculate_2x2_determinant()
            sign = (-1) ** (i + 2)
            self.determinant += sign * first_row[i] * minor
            if i != 2:
                # Deletes a single minor matrix
                del self.matrix[0]
                del self.matrix[0]
        self.matrix = original_matrix
        return self.determinant

    def extract_2x2_minor_matrices(self):
        """Extract the cofactor matrices of a 3x3 matrix.

        Return: list of all cofactor matrices (each 2x2), by row
        """
        if self.find_matrix_size() == 3:
            iteration = 1
            extract_result = [[], []]
            all_cofactor_matrices = []
            while iteration <= 3:
                for i in range(0, 2):
                    for j in range(0, 2):
                        # 3 cases for extracting the 3 cofactor matrices
                        if iteration == 1:
                            extract_result[i].append(self.matrix[i + 1][j + 1])
                        elif iteration == 2:
                            if j == 1:
                                extract_result[i].append(self.matrix[i + 1][j + 1])
                            else:
                                extract_result[i].append(self.matrix[i + 1][j])
                        if iteration == 3:
                            extract_result[i].append(self.matrix[i + 1][j])

                # Saves the found cofactor matrices
                for element in extract_result:
                    all_cofactor_matrices.append(element)
                extract_result = [[], []]
                iteration += 1
            return all_cofactor_matrices
