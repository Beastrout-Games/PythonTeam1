import unittest
from exercise2 import textClass

class TestUpper (unittest.TestCase):
        
    def test_getString(self):
        self.assertEqual(textClass.input(self), "ww")
        
    def test_printString(self):
        self.assertEqual(textClass.output(self, "ww"), "WW")
        
if __name__ == "__main__":
    unittest.main()
