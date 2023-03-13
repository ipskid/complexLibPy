# Readme for Python Complex Number Lib

This library is very simple; it implements the class Complex, which has two attributes to track the complex value: real and imag.
It also defines several basic functions to interact with instances of this class:

1. addComplex(a, b) performs the operation a+b
2. subComplex(a, b) performs the operation a-b
3. mulComplex(a, b) performs the operation a\*b
4. divComplex(a, b) performs the operation a/b
5. isEqual(a, b) compares the two complex numbers and returns true if they are equal

It should be noted that division by zero is handled by Python, requiring no further intervention.
Additional functionalities could include: retrieving abs and angle of the complex numbers, or implementing trigonometric operations to ease library usage for engineering purposes.
A final note is that 'i' was used instead of typical engineering 'j', mostly for aesthetic purposes, as this library printed complex numbers, and not variables or trig operations.

## Test file

A test file was created to demonstrate that the functions worked as intended, where arbitrary inputs were fed in, and the outputs were compared with the known output values.
Some sad test cases were also demonstrated, to show that errors are correctly handled by Python.
