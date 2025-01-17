import unittest
from main import add

class TestMain(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(5, 4), 9)
        self.assertEqual(add(5, 19), 24)

if __name__ == "__main__":
    unittest.main()
