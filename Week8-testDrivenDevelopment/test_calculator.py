import unittest
import calculator

# check the doc : https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug
class TestCalc(unittest.TestCase):
    
    def test_add(self):
        result = calculator.add(10, 5)
        self.assertEqual(result, 15)
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertEqual(calculator.add(-1, -1), -2)

    def test_substract(self):
        self.assertEqual(calculator.substract(10, 5), 5)    
        self.assertEqual(calculator.substract(-1, 1), -2)    
        self.assertEqual(calculator.substract(-1,-1), 0)    

    def test_multiply(self):
        self.assertEqual(calculator.multiply(10, 5), 50)    
        self.assertEqual(calculator.multiply(-1, 1), -1)    
        self.assertEqual(calculator.multiply(-1,-1), 1)    

    def test_divide(self):
        self.assertEqual(calculator.divide(10, 5), 2)    
        self.assertEqual(calculator.divide(-1, 1), -1)    
        self.assertEqual(calculator.divide(-1, -1), 1)    
        
if __name__ == '__main__':
    unittest.main()
