class Matrix:

    def __init__(self, rows, columns, name):
        self.rows = rows
        self.columns = columns
        self.determinant = None
        self.name = name
        self.matrix = []
        self.create_matrix()
        Matrix.display_matrix(self.matrix)

    def create_matrix(self):
        for i in range(0, self.rows):
            self.matrix.append([])

        # Prompts the user to input their desired matrix row by row """
        print("Enter the elements of matrix " + self.name + " by row:")

        for i in range(0, len(self.matrix)):    # len(self.matrix) = the number of rows of the matrix
            for j in range(0, self.columns):
                self.matrix[i].append(int(input()))

    # Displays relevant matrix to the user
    @staticmethod
    def display_matrix(matrix):
        rows = len(matrix)
        columns = len(matrix[0])

        for i in range(0, rows):
            for j in range(0, columns):
                print(str(matrix[i][j]), end='  ')
            print("")
        print("*" * 200)  # star line to improve output readability

    @staticmethod
    def add_matrices(x, y):
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

    def matrix_determinant(self):
        if self.find_matrix_size() == 2:
            self.determinant = self.calculate_2x2_determinant()
            print("Matrix " + self.name + " Determinant = " + str(self.determinant))

        elif self.find_matrix_size() == 3:
            first_row = self.matrix[0]
            cofactor_matrices = self.extract_2x2_cofactor_matrices()
            print("cofactor matrices: {}".format(cofactor_matrices))
            original_matrix = self.matrix
            self.matrix = cofactor_matrices

            self.determinant = 0
            for i in range(0, 3):
                minor = self.calculate_2x2_determinant()
                sign = (-1)**(i + 2)
                self.determinant += sign * first_row[i] * minor
                if i != 2:
                    del self.matrix[0]
                    del self.matrix[0]
            print("Matrix {} Determinant = {}".format(self.name, self.determinant))
            self.matrix = original_matrix

    def find_matrix_size(self):
        if self.rows == 2 and self.columns == 2:
            return 2

        elif self.rows == 3 and self.columns == 3:
            return 3

    def calculate_2x2_determinant(self):
        determinant = (self.matrix[0][0] * self.matrix[1][1]) - (self.matrix[1][0] * self.matrix[0][1])
        return determinant

    def extract_2x2_cofactor_matrices(self):
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


m = Matrix(3, 3, "A")
m.matrix_determinant()