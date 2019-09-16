#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 18:32:07 2019

@author: akshay.nadgire
"""

import numpy as np
import pandas as pd
import random

def f(x):
    return x**2

#%%
pop = np.random.randint(2, size=(8,4))

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
def selection(fitF, numSol):
    
    fit_sortF = fitF.sort_values(by = 2, ascending=False)
    
    for i in range(numSol):
        a = random.randint(0,numSol - 1)
        
        while a == i:
            a = random.randint(0,numSol - 1)
        
        if fitF.iloc[a,2] < fitF.iloc[i,2]:
            fit_sortF.iloc[i,:] = fitF.iloc[i,:]
        else:
            fit_sortF.iloc[i,:] = fitF.iloc[a,:]
    return fit_sortF

#%%
def crossover(new_pop_selF, numSol, bit, pcross):
    new_pop_crossF = new_pop_selF
    available = list(np.arange(numSol))
    
    for i in range(int(numSol / 2)):
        a = random.choice(available)
        available.remove(a)
        b = random.choice(available)
        available.remove(b)
        pc = pcross
        
        for j in range(1,bit):
            r = random.uniform(0,1)
            if r < pc:
                new_pop_crossF[a][j:bit] = new_pop_selF[b][j:bit]
                new_pop_crossF[b][j:bit] = new_pop_selF[a][j:bit]              
                break
    return new_pop_crossF

#%%
def mutation(new_pop_crossF, numSol, bit, pmut):
    new_pop_mutF = new_pop_crossF
    pm = pmut
    for i in range(numSol):
        for j in np.arange(bit):
            r = random.uniform(0,1)
            if r < pm:
                if new_pop_crossF[i][j] == 1:
                    new_pop_mutF[i][j] = 0
                else:
                    new_pop_mutF[i][j] = 1
                break
    return new_pop_mutF

#%%

fit = pd.DataFrame(np.zeros((8,3)))

for k in range(1000):
    for i in range(8):
        fit.iloc[i,0] = i
        fit.iloc[i,1] = bin2val(pop[i],-5,5,4)
        fit.iloc[i,2] = f(fit.iloc[i,1])
    
    fit_sort = (selection(fit, len(pop))).sort_values(by = 2, ascending=False)
    
    new_pop_sel = np.zeros_like(pop, dtype=int)
    for i in range(len(pop)):
        new_pop_sel[i] = pop[int(fit_sort.iloc[i,0])]
        
    new_pop_cross = crossover(new_pop_sel, len(pop), 4, 0.3)
    
    new_pop_mut = mutation(new_pop_cross, len(pop), 4, 0.125)
    
    pop = new_pop_mut

fit_sort.columns = ['SrNo','Value','Fitness']
print(fit_sort)