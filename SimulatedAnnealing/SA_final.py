#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 13:53:57 2019

@author: akshay.nadgire
"""

import numpy as np
import random

#Rosenbrock function with a=1, b=100
def f(x,y):
    return (1 - x)**2 + 100 * (y - x**2)**2
#%%
print("\n======================================")
print("\nOptimization by Simulated Annealing method\n")

#Initial temp, guess solution
T0 = 1000
x0 = 5
y0 = 5

#Function to calculate starting temp for annealing
def init_Temp(x0,y0,T0):
    m1 = 0
    m2 = 0
    Itr = 0
    rej_deltaE = []
    while True:
        Itr = Itr + 1
        x = x0 + random.uniform(-0.5,0.5)
        y = y0 + random.uniform(-0.5,0.5)
        r = random.uniform(0,1)
        
        deltaE = f(x,y) - f(x0,y0)
        
        if deltaE < 0:
            x0 = x
            y0 = y
            m1 = m1 + 1
        elif r < np.exp(-deltaE / T0):
            x0 = x
            y0 = y
            m1 = m1 + 1
        else:
            m2 = m2 + 1
            rej_deltaE.append(deltaE)
        
        if Itr > 499:
            break
        
    #print(m1,m2)
    T = (-np.mean(rej_deltaE)) / (np.log((-m1 + 0.95*500) / m2))
        
    return T

T = init_Temp(x0,y0,T0)

#Calculating min
maxItr = 2000
Lkmax = 50
minZita = 10
m = 0
Itr = 0
#T = T0

while True:
    Itr = Itr + 1
    L = 0
    Zita = 0
    while True:
        x = x0 + random.uniform(-0.5,0.5)
        y = y0 + random.uniform(-0.5,0.5)
        r = random.uniform(0,1)
        
        deltaE = f(x,y) - f(x0,y0)
        
        if deltaE < 0:
            x0 = x
            y0 = y
            m = m + 1
        elif r < np.exp(-deltaE / T):
            x0 = x
            y0 = y
            m = m + 1
            
        L = L + 1
        Zita = Zita + m
        
        if L >= Lkmax or Zita >= minZita:
            break
    T = T * 0.8
    
    if Itr >= maxItr:
        break
    
print("Minima is at x = %f, y = %f"%(x0, y0))
print("Function value at minima is %f"%f(x0,y0))
print("\n======================================")