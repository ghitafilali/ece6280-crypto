import unittest
import problem1
import numpy as np


class TestProblem1(unittest.TestCase):
    """
    Test problem 1 functions.
    """
    def test_binary_cartesian_product(self):
        product_of_two = set([(0,0), (0, 1), (1, 0), (1, 1)])
        self.assertEqual(set(problem1.binary_cartesian_product(2)), product_of_two)

        product_of_three = set([(0, 0, 0),
                                (0, 0, 1),
                                (0, 1, 0),
                                (0, 1, 1),
                                (1, 0, 0),
                                (1, 0, 1),
                                (1, 1, 0),
                                (1, 1, 1)])
        self.assertEqual(set(problem1.binary_cartesian_product(3)), product_of_three)

    def test_x_generator(self):
        x_sequence = [1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0]
        x_init = x_sequence[:3]
        x_counter = 0
        x_list = list(x_init)
        for i in range(len(x_sequence)):
            res, x_counter, x_list = problem1.x_generator(x_init, x_counter, x_list).__next__()
            self.assertEqual(x_sequence[i], res)

    def test_y_generator(self):
        y_sequence = [1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1]
        y_init = y_sequence[:4]
        y_counter = 0
        y_list = list(y_init)
        for i in range(len(y_sequence)):
            res, y_counter, y_list = problem1.y_generator(y_init, y_counter, y_list).__next__()
            self.assertEqual(y_sequence[i], res)

    def test_z_generator(self):
        z_sequence = [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1]
        z_init = z_sequence[:5]
        z_counter = 0
        z_list = list(z_init)
        for i in range(len(z_sequence)):
            res, z_counter, z_list = problem1.z_generator(z_init, z_counter, z_list).__next__()
            self.assertEqual(z_sequence[i], res)

    def test_generate_x_stream(self):
        x_sequence_verify = [1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0]
        initial = x_sequence_verify[:3]
        self.assertEqual(x_sequence_verify, problem1.generate_x_stream(initial,
                                                                       len(x_sequence_verify)))

    def test_generate_y_stream(self):
        y_sequence_verify = [1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1]
        initial = y_sequence_verify[:4]
        self.assertEqual(y_sequence_verify, problem1.generate_y_stream(initial,
                                                                       len(y_sequence_verify)))

    def test_generate_z_stream(self):
        z_sequence_verify = [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1]
        initial = z_sequence_verify[:5]
        self.assertEqual(z_sequence_verify, problem1.generate_z_stream(initial,
                                                                       len(z_sequence_verify)))