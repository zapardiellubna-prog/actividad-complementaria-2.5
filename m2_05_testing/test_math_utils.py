import unittest 
from math_utils import suma, resta, multiplicacion, division 

class TestMathUtilsValidos(unittest.TestCase): 
    def test_suma(self): 
        self.assertEqual(suma(2, 3), 5) 
        self.assertAlmostEqual(suma(2.5, 0.1), 2.6, places=7) 

    def test_resta(self): 
        self.assertEqual(resta(5, 2), 3) 
        self.assertAlmostEqual(resta(2.5, 0.5), 2.0) 

    def test_multiplicacion(self): 
        self.assertEqual(multiplicacion(3, 4), 12) 
        self.assertAlmostEqual(multiplicacion(2.5, 2), 5.0) 

    def test_division(self): 
        self.assertAlmostEqual(division(10, 2), 5.0) 
        self.assertAlmostEqual(division(1, 4), 0.25) 

class TestMathUtilsInvalidos(unittest.TestCase): 
    def test_tipos_invalidos(self): 
        with self.assertRaises(TypeError): 
            suma("2", 3) 
        with self.assertRaises(TypeError): 
            resta(1, None) 
        with self.assertRaises(TypeError): 
            multiplicacion([], {}) 
        with self.assertRaises(TypeError): 
            division("10", "2") 

    def test_division_por_cero(self): 
        with self.assertRaises(ZeroDivisionError): 
            division(5, 0) 
        with self.assertRaises(ZeroDivisionError): 
            division(0.0, 0) 

if __name__ == "__main__": 
    unittest.main()