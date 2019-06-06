import unittest
class CheckNumbers(unittest.TestCase):
    def test_int_float(self):
        self.assertEquals(1, 1.0)

    def test_str_float(self):
        self.assertNottesEquals("1", 1.0)

    def test_bolean_float(self):
        self.assertEquals(3/2, 1.5)

    def test_int_str(self):
        self.assertNotEquals(1, "1")

if __name__ == "__main__":
    unittest.main() 