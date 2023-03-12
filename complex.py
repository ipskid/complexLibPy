class Complex:
    def __init__(self, realPart, imagPart):
        self.real = realPart
        self.imag = imagPart
    
    def __str__(self):
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
    return Complex(a.getReal()+b.getReal(), a.getImag()+b.getImag())

def subComplex(a, b):
    return Complex(a.getReal()-b.getReal(), a.getImag()-b.getImag())

def mulComplex(a, b):
    real = a.getReal()*b.getReal() - a.getImag()*b.getImag()
    imag = a.getReal()*b.getImag() + a.getImag()*b.getReal()
    return Complex(real, imag)

def divComplex(a, b):
    real = (a.getReal()*b.getReal() + a.getImag()*b.getImag())/(b.getReal()**2+b.getImag()**2)
    imag = (a.getImag()*b.getReal() - a.getReal()*b.getImag())/(b.getReal()**2+b.getImag()**2)
    return Complex(real, imag)
    
a = Complex(1,-1)
b = Complex(0,0)

print(addComplex(a,b))
print(subComplex(a,b))
print(mulComplex(a,b))

try:
    print(divComplex(a,b))
except ZeroDivisionError:
    print("Division by zero")

#add tests for simple operations with expected results