from unittest import TestCase

from main import (
    triangle_type,
    TYPE_SCALENE,
    TYPE_ISOSCELES,
    TYPE_EQUILATERAL,
    NOT_A_TRIANGLE,
    MSG_INVALID_RANGE,
    MSG_INVALID_INPUT,
)


class TestTriangle(TestCase):
    def test_equilateral_triangle(self):
        self.assertEqual(triangle_type(5, 5, 5), TYPE_EQUILATERAL)

    def test_isosceles_triangle(self):
        self.assertEqual(triangle_type(5, 5, 8), TYPE_ISOSCELES)
        self.assertEqual(triangle_type(8, 5, 5), TYPE_ISOSCELES)
        self.assertEqual(triangle_type(5, 8, 5), TYPE_ISOSCELES)

    def test_scalene_triangle(self):
        self.assertEqual(triangle_type(3, 4, 5), TYPE_SCALENE)

    def test_not_a_triangle(self):
        self.assertEqual(triangle_type(1, 2, 3), NOT_A_TRIANGLE)
        self.assertEqual(triangle_type(1, 1, 2), NOT_A_TRIANGLE)

    def test_values_out_of_range(self):
        self.assertEqual(triangle_type(0, 5, 5), MSG_INVALID_RANGE)
        self.assertEqual(triangle_type(5, 0, 5), MSG_INVALID_RANGE)
        self.assertEqual(triangle_type(5, 5, 0), MSG_INVALID_RANGE)
        self.assertEqual(triangle_type(201, 5, 5), MSG_INVALID_RANGE)

    def test_invalid_input(self):
        self.assertEqual(triangle_type("a", 5, 5), MSG_INVALID_INPUT)
        self.assertEqual(triangle_type(5, "b", 5), MSG_INVALID_INPUT)
        self.assertEqual(triangle_type(5, 5, "c"), MSG_INVALID_INPUT)
