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
        if x.rows == y.rows and x.columns == y.columns:
            result = [[], []]
            for i in range(0, x.rows):
                for j in range(0, y.columns):
                    result[i].append(x.matrix[i][j] + y.matrix[i][j])

            print("RESULT OF ADDITION: " + x.name + " + " + y.name)
            for i in range(0, 2):
                for j in range(0, 2):
                    print(str(result[i][j]), end='  ')
                print("")
        else:
            print("Matrix " + x.name + " and " + y.name + " must have the same dimensions")

m1 = Matrix(2, 2, "A")
m2 = Matrix(2, 2, "B")
Matrix.add_matrices(m1, m2)
