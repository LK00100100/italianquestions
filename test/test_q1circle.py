from unittest import TestCase

from q1circle import solution


class TestQ1Circle(TestCase):

    def test_solution_1(self):
        s = "ABDCA"
        x = [2, -1, -4, -3, 3]
        y = [2, -2, 4, 1, -3]
        answer = solution(s, x, y)

        expected = 3
        self.assertEqual(expected, answer)

    def test_solution_2(self):
        s = "ABB"
        x = [1, -2, -2]
        y = [1, -2, 2]
        answer = solution(s, x, y)

        expected = 1
        self.assertEqual(expected, answer)
