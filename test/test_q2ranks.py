from unittest import TestCase

from q2ranks import solution


class TestQ2Ranks(TestCase):

    def test_solution_1(self):
        ranks = [3, 4, 3, 0, 2, 2, 3, 0, 0]
        answer = solution(ranks)

        expected = 5
        self.assertEqual(expected, answer)

    def test_solution_2(self):
        ranks = [4, 2, 0]
        answer = solution(ranks)

        expected = 0
        self.assertEqual(expected, answer)

    def test_solution_3(self):
        ranks = [4, 4, 3, 3, 1, 0]
        answer = solution(ranks)

        expected = 3
        self.assertEqual(expected, answer)
