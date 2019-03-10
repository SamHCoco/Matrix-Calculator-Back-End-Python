from MatrixCalculator_Back_End import *
import unittest


class TestMatrixCalculator(unittest.TestCase):

    def test_add_matrices(self):
        """"Test matrix + matrix."""
        self.m4 = Matrix(4, 4, "A4")
        self.m4.matrix = [[1,  2,  3,  4],
                          [5,  6,  7,  8],
                          [9,  10, 11, 12],
                          [13, 14, 15, 16]]
        expected_result = [[2.0,  4.0,  6.0,  8.0],
                           [10.0, 12.0, 14.0, 16.0],
                           [18.0, 20.0, 22.0, 24.0],
                           [26.0, 28.0, 30.0, 32.0]]
        self.assertEqual(Matrix.add_matrices(self.m4, self.m4), expected_result)
        self.m4.matrix = [[0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 0]]
        expected_result = [[0.0, 0.0, 0.0, 0.0],
                           [0.0, 0.0, 0.0, 0.0],
                           [0.0, 0.0, 0.0, 0.0],
                           [0.0, 0.0, 0.0, 0.0]]
        self.assertEqual(Matrix.add_matrices(self.m4, self.m4), expected_result)

