from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution

        my_tuple = ([8, 4, 6], [1, 2, 3])

        result = solution(my_tuple)

        self.assertNotEqual(None, result)

        self.assertEqual(result[0][0], 8)
        self.assertEqual(result[0][1], 4)
        self.assertEqual(result[0][2], 6)
        self.assertEqual(result[1][0], 1)
        self.assertEqual(result[1][1], 2)
        self.assertEqual(result[1][2], 3)
