# https://github.com/kwongosint/lab11-KW-CC
# Partner 1: Connor Corr
# Partner 2: Katie Wong

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def add(a, b): 
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b 

def div(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a/b

def log(a, base):
    if a <= 0 or base <= 0 or base == 1:
        raise ValueError("Logarithm undefined for non-positive numbers")
    return math.log(a, base)

def exp(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        raise ValueError("Square root undefined for negative numbers")
    return math.sqrt(a)

def hypotenuse(a,b):
    return math.hypot(a,b)

