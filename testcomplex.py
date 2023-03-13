import complex as c
import unittest

class TestComplexFunctions(unittest.TestCase):

    def test_add_complex(self):
        # Setup A + B = output
        inputA = [[1,1], [-4,9], [-1,-2], [2,-9]]
        inputB = [[0,2], [1,-1], [0,1.0], [10,0]]
        output = [[1,3], [-3,8], [-1,-1], [12,-9]] # Easily verifiable as correct
        complexInputA = []
        complexInputB = []
        complexOutput = []
        for idx in range(len(output)): # Assumption: output array has same number of elements are input arrays
            complexInputA.append(c.Complex(*inputA[idx]))
            complexInputB.append(c.Complex(*inputB[idx]))
            complexOutput.append(c.Complex(*output[idx]))
        
        # Assertions
        for idx in range(len(output)):
            self.assertTrue( c.isEqual(c.addComplex( complexInputA[idx],complexInputB[idx] ), complexOutput[idx]) )

    def test_sub_complex(self):
        # Setup A - B = output
        inputA = [[1,1],  [-4,9],  [-1,-2], [2,-9]] # Inputs could be different per test case, but I left them
        inputB = [[0,2],  [1,-1],  [0,1.0], [10,0]] # the same for this example.
        output = [[1,-1], [-5,10], [-1,-3], [-8,-9]]
        complexInputA = []
        complexInputB = []
        complexOutput = []
        for idx in range(len(output)):
            complexInputA.append(c.Complex(*inputA[idx]))
            complexInputB.append(c.Complex(*inputB[idx]))
            complexOutput.append(c.Complex(*output[idx]))
        
        # Assertions
        for idx in range(len(output)):
            self.assertTrue( c.isEqual(c.subComplex( complexInputA[idx],complexInputB[idx] ), complexOutput[idx]) )

    def test_mul_complex(self):
        # Setup A * B = output
        inputA = [[1,1],  [-4,9], [-1,-2], [2,-9]]
        inputB = [[0,2],  [1,-1], [0,1.0], [10,0]]
        output = [[-2,2], [5,13], [2,-1],  [20,-90]] # Results were calculated with Wolfram Alpha
        complexInputA = []
        complexInputB = []
        complexOutput = []
        for idx in range(len(output)):
            complexInputA.append(c.Complex(*inputA[idx]))
            complexInputB.append(c.Complex(*inputB[idx]))
            complexOutput.append(c.Complex(*output[idx]))
        
        # Assertions
        for idx in range(len(output)):
            self.assertTrue( c.isEqual(c.mulComplex( complexInputA[idx],complexInputB[idx] ), complexOutput[idx]) )

    def test_div_complex(self):
        # Setup A / B = output
        inputA = [[1,1],      [-4,9],     [-1,-2], [2,-9]]
        inputB = [[0,2],      [1,-1],     [0,1.0], [10,0]]
        output = [[0.5,-0.5], [-6.5,2.5], [-2,1],  [0.2,-0.9]] # Results were calculated with Wolfram Alpha
        complexInputA = []
        complexInputB = []
        complexOutput = []
        for idx in range(len(output)):
            complexInputA.append(c.Complex(*inputA[idx]))
            complexInputB.append(c.Complex(*inputB[idx]))
            complexOutput.append(c.Complex(*output[idx]))
        
        # Assertions
        for idx in range(len(output)):
            self.assertTrue( c.isEqual(c.divComplex( complexInputA[idx],complexInputB[idx] ), complexOutput[idx]) )

    def test_float_string_input(self):
        # Setup for showing any valid real number can be input, even as a string; exemplified with addition
        complexInputA = c.Complex("1",    42.0)
        complexInputB = c.Complex(-5.12,"-5.4")
        complexOutput = c.Complex(-4.12,  36.6)
        self.assertTrue( c.isEqual(c.addComplex( complexInputA, complexInputB), complexOutput) )

    def test_sad_case_input_string(self):
        # Setup for triggering a string that cannot be interpreted as a real number
        with self.assertRaises(ValueError):
            c.Complex("asdf",0)

    def test_sad_case_div_by_zero(self):
        # Setup for demonstrating that division by zero was considered and is caught by Python
        complexInputA = c.Complex(1,1)
        complexInputB = c.Complex(0,0)
        with self.assertRaises(ZeroDivisionError):
            c.divComplex(complexInputA,complexInputB)

if __name__ == '__main__':
    unittest.main()