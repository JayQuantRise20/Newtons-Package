import pandas as pd
import numpy as np


class Newton_Method():
    def __init__(self,function,iterations=100,initial_point = 1):
    
        self.x0 = initial_point
        self.n = iterations
        self.f = function
    
    def f_derivative(self,f,x):
        h = 1/1000
        
        return (f(x+h)-f(x))/h
        
    def Calculate_root(self):
        x_prime = self.x0
        for i in np.arange(self.n):
            x_prime = x_prime - (self.f(x_prime)/self.f_derivative(self.f,x_prime))
        
        return x_prime
        