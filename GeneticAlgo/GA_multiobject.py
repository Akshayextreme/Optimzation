#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 14:28:26 2019

@author: akshay.nadgire
"""

import numpy as np

def f1(x):
    return x**2

def f2(x):
    return (x - 2)**2

#%%
def bin2val(num,lower,upper,bit):
    dig = 0
    tmp = 0
    summ = 0
    for j in np.arange(bit-1,-1,-1):
        dig = num[j]
        tmp = dig * 2**((bit-1) - j)
        summ = summ + tmp
    
    return lower + ((upper - lower) / (2**bit - 1)) * summ
#%%
pop = np.random.randint(2, size=(8,4))

fvalue = np.zeros((8,4))

for i in range(8):
    fvalue[i,0] = i
    fvalue[i,1] = bin2val(pop[i], -5, 5, 4)
    fvalue[i,2] = f1(fvalue[i,1])
    fvalue[i,3] = f2(fvalue[i,1])

Np = np.copy(fvalue)
Np1 = np.zeros_like(Np)
Np2 = np.zeros_like(Np)

available = list(np.arange(8))

k = 0
p=0
for i in range(4):
    a = np.random.choice(available)
    available.remove(a)
    b = np.random.choice(available)
    available.remove(b)
    
    ind = [a,b]
    nxt_itr = []
    
    Np1[k,:] = Np[ind[0],:]
    Np1[k+1,:] = Np[ind[1],:]
    k = k + 2
    
    for l in range(2):
        non = 0
        c = ind[l]
        dec = []
        if np.sum(Np[c,2:4] <= Np[ind[0],2:4]) == 0:
            continue
            
        if np.sum(Np[c,2:4] <= Np[ind[1],2:4]) == 0:  
            continue
            
        for j in range(p):
            if np.sum(Np[c,2:4] <= Np2[j,2:4]) == 0:
                non = 1
                break
                
        if non == 0:
            Np2[p,:] = Np[c,:]
            p = p+1