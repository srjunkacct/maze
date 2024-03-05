import unittest

from Key import Key


class MyTestCase(unittest.TestCase):
    def test_something(self):
        key0 = Key(0,0)
        key1 = Key(1,0)
        key2 = Key(0,0)
        key3 = Key(0,1)
        self.assertTrue(key0 == key2)
        self.assertFalse(key0 == key1)
        self.assertFalse(key0 == key3)


if __name__ == '__main__':
    unittest.main()
