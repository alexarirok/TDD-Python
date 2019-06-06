import unittest
from app.stat import Starlist

class TestValidInputs(unittest.TestCase):
    def setUp(self):
        self.stat = Starlist([1, 2, 2, 3, 3, 4])

    def test_mean(self):
        self.assertEqual(self.stat.mean(),2.5)
    
    def test_median(self):
        self.assertEqual(self.stat.median(),2.5)
        self.stat.append(4)
        self.assertEqual(self.stat.median(),3)

    def test_mode(self):
        self.stat.remove(2)
        #self.assertEqual(self.stat.mode(),[2, 3])
        self.assertEqual(self.stat.mode(),[3])

if __name__ == "__main__":
    unittest.main()


