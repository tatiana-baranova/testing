import unittest
import main

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEquals(main.add(5, 7), 12)
        self.assertEquals(main.add(5), 5)
        self.assertEquals(main.add(), 0)