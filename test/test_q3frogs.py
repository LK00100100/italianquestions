from unittest import TestCase

from q3frogs import solution


class TestQ3Frogs(TestCase):

    def test_solution_1(self):
        blocks = [2, 6, 8, 5]
        answer = solution(blocks)

        expected = 3
        self.assertEqual(expected, answer)

    def test_solution_2(self):
        blocks = [1, 5, 5, 2, 6]
        answer = solution(blocks)

        expected = 4
        self.assertEqual(expected, answer)

    def test_solution_3(self):
        blocks = [1, 1]
        answer = solution(blocks)

        expected = 2
        self.assertEqual(expected, answer)
