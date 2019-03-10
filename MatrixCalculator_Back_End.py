class Matrix:
    """ Define a matrix and its operations (Add, multiply etc).
    Attributes:
        rows (int) -- the number rows in the matrix
        columns (int)-- the number of columns in the matrix
        determinant (float)-- the matrix determinant
        name (string)-- the name of matrix
        matrix (list) -- the matrix values
    """

    def __init__(self, rows, columns, name, testing=True):
        """create matrix instance.
        Args:
           rows (int) -- matrix rows
           columns (int)-- matrix columns
           name (string) -- matrix name.
           testing (Boolean) -- For unit testing. Removed later.
        """
        self.rows = rows
        self.columns = columns
        self.determinant = None
        self.name = name
        self.matrix = []
        if not testing:
            self.create_matrix()
            Matrix.display_matrix(self.matrix)

    def create_matrix(self):
        """Input matrix values."""
        for i in range(0, self.rows):
            self.matrix.append([])
        print("Enter the elements of matrix " + self.name + " by row:")
        for i in range(0, self.rows):
            for j in range(0, self.columns):
                self.matrix[i].append(float(input()))

    @staticmethod
    def display_matrix(matrix):
        """Display inputted matrix."""
        rows = len(matrix)
        columns = len(matrix[0])
        for i in range(0, rows):
            for j in range(0, columns):
                print("{:>4}".format(matrix[i][j]), end=' ')
            print("")
        print("*" * 200)  # star line to improve output readability

    @staticmethod
    def add_matrices(x, y):
        """Add two matrices and display the result.
        Args:
           x -- A matrix of size NxN (N >= 2).
           y -- A matrix of size NxN (N >= 2).
        """
        added_matrix = []
        if x.rows == y.rows and x.columns == y.columns:
            # creates empty matrix that will contain result of addition
            for i in range(0, x.rows):
                added_matrix.append([])
            # performs matrix addition calculation
            for i in range(0, x.rows):
                for j in range(0, y.columns):
                    added_matrix[i].append(x.matrix[i][j] + y.matrix[i][j])
            print("RESULT OF ADDITION: " + x.name + " + " + y.name)
            Matrix.display_matrix(added_matrix)
        else:
            print("Matrix " + x.name + " and " + y.name + " must have the same dimensions")
        return added_matrix

    @staticmethod
    def scalar_multiply(scalar, matrix):
        """Multiply a matrix by a scalar and print result.
        Args:
            scalar -- the value that will multiply the matrix.
            matrix -- the matrix to be multiplied by scalar.
        """
        multiplied_matrix = []
        # Creates matrix needed to store final result
        for i in range(0, matrix.rows):
            multiplied_matrix.append([])
        # performs multiplication calculation
        for i in range(0, matrix.rows):
            for j in range(0, matrix.columns):
                multiplied_matrix[i].append(scalar * matrix.matrix[i][j])
        print("RESULT OF SCALAR MULTIPLICATION: {} x {}".format(scalar, matrix.name))
        Matrix.display_matrix(multiplied_matrix)
        return multiplied_matrix

    def find_matrix_size(self):
        """Determine dimensions of an NxN matrix (N >= 2).

           Returns: dimension of matrix (int value).
        """
        if self.rows == 2 and self.columns == 2:
            return 2
        elif self.rows == 3 and self.columns == 3:
            return 3

    def determinant(self):
        """Calculate matrix determinant."""
        if self.find_matrix_size() == 2:
            self.determinant = self.calculate_2x2_determinant()
            print("Matrix {} Determinant = {:.3f}".format(self.name, self.determinant))
        elif self.find_matrix_size() == 3:
            self.determinant = self.calculate_3x3_determinant()
            print("Matrix {} Determinant = {:.3f}".format(self.name, self.determinant))

    def calculate_2x2_determinant(self):
        """Calculate 2x2 matrix determinant."""
        determinant = (self.matrix[0][0] * self.matrix[1][1]) - (self.matrix[1][0] * self.matrix[0][1])
        return determinant

    def calculate_3x3_determinant(self):
        """Calculate 3x3 matrix determinant."""
        first_row = self.matrix[0]
        cofactor_matrices = self.extract_2x2_cofactor_matrices()
        print("cofactor matrices: {}".format(cofactor_matrices))
        original_matrix = self.matrix
        self.matrix = cofactor_matrices
        determinant = 0
        for i in range(0, 3):
            minor = self.calculate_2x2_determinant()
            sign = (-1) ** (i + 2)
            determinant += sign * first_row[i] * minor
            if i != 2:
                del self.matrix[0]
                del self.matrix[0]
        self.matrix = original_matrix
        return determinant

    def extract_2x2_cofactor_matrices(self):
        """Extract the cofactor matrices of a 3x3 matrix.

        returns: list of 3 cofactor matrices (each 2x2), by row."""
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
