#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 14:02:12 2019

@author: akshay.nadgire
"""

import numpy as np
import random

#Rosenbrock function with a=1, b=100
def f(x,y):
    return (1 - x)**2 + 100 * (y - x**2)**2
#%%
    print("\n======================================")
print("\nOptimization by Monte Carlo method\n")
#Initial guess solution
x0 = 5
y0 = 5
Itr = 0
maxItr = 5000

#Calculating min
while True:
    x = x0 + random.uniform(-0.5,0.5)
    y = y0 + random.uniform(-0.5,0.5)
        
    deltaE = f(x,y) - f(x0,y0)
    
    if deltaE < 0:
        #print(deltaE)
        x0, y0 = x, y
        
    Itr = Itr + 1
    
    if Itr > maxItr:
        break

print("Minima is at x = %f, y = %f"%(x0, y0))
print("Function value at minima is %f"%f(x0,y0))

#%%
print("\n======================================")
print("\nOptimization by Metropolis Monte Carlo method\n")
#Initial guess solution
x0 = 5
y0 = 5
Itr = 0
maxItr = 5000

#Calculating min
while True:
    x = x0 + random.uniform(-0.5,0.5)
    y = y0 + random.uniform(-0.5,0.5)
    r = random.uniform(0,1)
        
    deltaE = f(x,y) - f(x0,y0)
    
    if deltaE < 0:
            x0 = x
            y0 = y
    elif r < np.exp(-deltaE):
            x0 = x
            y0 = y
        
    Itr = Itr + 1
    
    if Itr > maxItr:
        break

print("Minima is at x = %f, y = %f"%(x0, y0))
print("Function value at minima is %f"%f(x0,y0))