import pandas as pd
import numpy as np

def f_derivative(f,x):
    h = 1/1000

    return (f(x+h)-f(x))/h
def f(x):
    return x**2-100

def f_derivative(f,x):
    h = 1/1000
    return (f(x+h)-f(x))/h

x0 = 0
def Newton_method(x0):
    x_prime = x0
    for i in np.arange(20):
        x_prime = x_prime - (f(x_prime)/f_derivative(f,x_prime))
    return x_prime
