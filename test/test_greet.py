import unittest

from greet import greet


class TestGreet(unittest.TestCase):

    def test_david(self):
        self.assertEqual(greet('David'), 'Hello David!')


if __name__ == '__main__':
    unittest.main()
