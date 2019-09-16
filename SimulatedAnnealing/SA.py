#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 22:37:33 2019

@author: akshay.nadgire
"""

import numpy as np
import random

def f(x,y):
    return (1 - x)**2 + 100 * (y - x**2)**2

T0 = 1000
x0 = 5
y0 = 5

maxItr = 2000
Lkmax = 50
minZita = 10
m = 0
Itr = 0
T = T0

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
    
print(x0,y0)
print(f(x0,y0))