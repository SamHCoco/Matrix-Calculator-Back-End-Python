from MatrixCalculator_Back_End import *
import unittest


class TestMatrixCalculator(unittest.TestCase):

    # Create
    def setUp(self):
        """Sets up test case values for tests."""
        # 3x3 matrix test case
        self.matrix_1 = Matrix(3, 3, "A(3x3)", testing=True)
        self.matrix_1.matrix = [[1.11, 2.22, -3.338],
                                [4.44, 5.55,  -6],
                                [0,    7.77,  -8.88]]
        # 2x2 matrix test case
        self.matrix_2 = Matrix(2, 2, "B(2x2)", testing=True)
        self.matrix_2.matrix = [[1.111, 2.222],
                                [3.333, -4.444]]

    def test_add(self):
        """"Test matrix + matrix."""
        expected_result = [[2.22,  4.44,  -6.676],
                           [8.88, 11.1, -12.0],
                           [0, 15.54, -17.76]]
        self.assertEqual(self.matrix_1.add(self.matrix_1), expected_result)

    def test_scalar_multiply(self):
        """ Test scalar multiplication, 3 * matrix."""
        expected_result = [[3.33,  6.66,  -10.014],
                           [13.32, 16.65, -18],
                           [0,     23.31, -26.64]]
        self.assertEqual(self.matrix_1.scalar_multiply(3), expected_result)

    def test_multiply(self):
        """Test matrix multiplication."""
        expected_result = [[11.089, -11.151, 12.616],
                           [29.570, -5.961, 5.159],
                           [34.499, -25.874, 32.234]]
        self.assertEqual(self.matrix_1.multiply(self.matrix_1), expected_result)

    def test_find_determinant(self):
        """Test finding 3x3 and 2x2 matrix determinant."""
        # 3x3 case
        self.assertEqual(self.matrix_1.find_determinant(), -30.586)
        # 2x2 case
        self.assertEqual(self.matrix_2.find_determinant(), -12.343)

    def test_find_matrix_size(self):
        """Test finding matrix size."""
        self.assertEqual(self.matrix_1.find_matrix_size(), 3)
        matrix = Matrix(4, 4, "C")
        matrix.matrix = [[1, 2, 3, 4],
                         [5, 6, 7, 8],
                         [9, 10, 11, 12],
                         [13, 14, 15, 16]]
        self.assertEqual(matrix.find_matrix_size(), -1)

    def test_dot_product(self):
        """Test finding dot product between two vectors."""
        vector_1 = [1.1111, 2.2222, 3.3333]
        vector_2 = [1.1111, 2.2222, 3.33333]
        self.assertEqual(Matrix.dot_product(vector_1, vector_2), 17.284)
        # case for incorrect vector size
        vector_2 = [1, 2, 3, 4]
        self.assertEqual(Matrix.dot_product(vector_1, vector_2), -1)

