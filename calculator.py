"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
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
    if a <= 0:
        raise ValueError("Logarithm undefined for non-positive numbers")
    return math.log(a, base)

def exp(a, b):
    return a ** b

