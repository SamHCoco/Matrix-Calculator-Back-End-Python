class Matrix:

    def __init__(self, rows, columns, name):
        self.rows = rows
        self.columns = columns
        self.name = name
        self.matrix = []
        self.create_matrix()
        self.display_matrix()

    def create_matrix(self):
        # Inserts lists to existing empty list. Each appended lists contains the row of a matrix
        for i in range(0, self.rows):
            self.matrix.append([])

        # Prompts the user to input their desired matrix row by row """
        print("Enter the elements of matrix " + self.name + " by row:")
        for i in range(0, len(self.matrix)):    # len(self.matrix) = the number of rows of the matrix
            for j in range(0, self.columns):
                self.matrix[i].append(int(input()))

        # Displays the user's inputted matrix"""
    def display_matrix(self):
        print("Matrix " + self.name + ":")
        for i in range(0, len(self.matrix)):  # len(self.matrix) = the number of rows of the matrix
            for j in range(0, self.columns):
                print(str(self.matrix[i][j]), end='  ')
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
            for i in range(0, 2):
                for j in range(0, 2):
                    print(str(added_matrix[i][j]), end='  ')
                print("")
        else:
            print("Matrix " + x.name + " and " + y.name + " must have the same dimensions")

    def calculate_determinant(self):
        first_row = [self.matrix[0]]  # 1st row of the matrix
        other_rows = [self.matrix[1], self.matrix[2]]  # 2nd and 3rd rows of the matrix
        cofactor_matrices = []  # The elements of the cofactor matrices of the matrix
        matrix_cofactors = []  # The actual cofactors of the matrix

        # Determinant for a 2x2 matrix
        if self.rows == 2 and self.columns == 2:
            result = (self.matrix[0][0] * self.matrix[1][1]) - (self.matrix[1][0] * self.matrix[0][1])

        # Determinant for a 3x3 matrix
        elif self.rows == 3 and self.columns == 3:
            for row in first_row:
                for value_1 in row:
                    for element in other_rows:
                        for value_2 in element:
                            if row.index(value_1) != element.index(value_2):
                                cofactor_matrices.append(value_2)

            print(cofactor_matrices)  # for debugging

            # Calculates the 2x2 determinant of each cofactor matrix
            for i in range(0, 12, 4):
                cofactor_matrix = cofactor_matrices[i: i + 4]
                matrix_cofactors.append(
                    cofactor_matrix[0] * cofactor_matrix[3] - cofactor_matrix[2] * cofactor_matrix[1])
            print("Matrix " + self.name + " cofactors: " + str(matrix_cofactors))

            # Calculates the final result (determinant of the 3x3 matrix)
            result = 0
            for i in range(0, 3):
                result += ((-1) ** i) * matrix_cofactors[i] * self.matrix[0][i]
            print("Det({}) = {}".format(self.name, result))

m1 = Matrix(3, 3, "A")
m1.calculate_determinant()



