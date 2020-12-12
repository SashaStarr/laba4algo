import unittest
from algoritm import read_csv_file, longest_chain


class AlgoTest(unittest.TestCase):
    def test_longest_chain(self):
        self.assertEqual(1, longest_chain(read_csv_file()))


if __name__ == '__main__':
    unittest.main()
