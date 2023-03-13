class Complex:
    def __init__(self, realPart, imagPart):
        self.real = float(realPart) # Sanitize if string is input
        self.imag = float(imagPart)
    
    def __str__(self):
        # To print, returns in the form of (real) (sign) (imag)i, where the sign is omitted if -, as it is already shown in the number
        return '{r}{op}{i}i'.format(r = self.real, i = self.imag, op = '+' if self.imag >= 0 else '')
    
    def getReal(self):
        return self.real
    
    def getImag(self):
        return self.imag
    
    def setReal(self):
        return self.real
    
    def setImag(self):
        return self.imag

def addComplex(a, b):
    # Addition is simply Re{a}+Re{b} + (Im{a}+Im{b})i
    return Complex(a.getReal()+b.getReal(), a.getImag()+b.getImag())

def subComplex(a, b):
    # Subtraction refers to a-b
    return Complex(a.getReal()-b.getReal(), a.getImag()-b.getImag())

def mulComplex(a, b):
    # Complex multiplication observes the distributive property
    real = a.getReal()*b.getReal() - a.getImag()*b.getImag()
    imag = a.getReal()*b.getImag() + a.getImag()*b.getReal()
    return Complex(real, imag)

def divComplex(a, b):
    # Complex division is expanded from numerator/denominator to this formula
    real = (a.getReal()*b.getReal() + a.getImag()*b.getImag())/(b.getReal()**2+b.getImag()**2)
    imag = (a.getImag()*b.getReal() - a.getReal()*b.getImag())/(b.getReal()**2+b.getImag()**2)
    return Complex(real, imag)

def isEqual(a, b):
    # Useful function to check if complex numbers are equal, used for testing
    return a.getReal() == b.getReal() and a.getImag() == b.getImag()