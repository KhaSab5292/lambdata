import unittest
from df_utils import find_seconds


class Seconds_test(unittest.TestCase):
    """Obligatory docstring test root function!"""
    def test_minute(self):
        self.assertEqual(find_seconds(0, 0, 1, 0), 60)

    def test_hour(self):
        self.assertEqual(find_seconds(0, 1, 0, 0), 3600)

    def test_ones(self):
        self.assertEqual(find_seconds(1, 1, 1, 1), 90061)

if __name__ == '__main__':
    unittest.main()
