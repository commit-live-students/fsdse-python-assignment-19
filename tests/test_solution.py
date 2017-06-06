from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution

        dic1 = {10:1, 20:2, 30:3}
        key1 = 10
        key2 = 40
        res1 = solution(dic1, key1)
        res2 = solution(dic1, key2)

        self.assertEqual(res1, True)
        self.assertEqual(res2, False)
