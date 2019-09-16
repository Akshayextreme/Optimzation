#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 15:13:20 2019

@author: akshay.nadgire
"""

import numpy as np
import pandas as pd
import random
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, make_scorer
from sklearn.svm import SVC
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
def svm_cv(X, y, chromo):
    tot = X.shape[1]
    X = X[:,np.where(chromo == 1)[0]]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, \
                                                        random_state=44)
    
    model = SVC(kernel='rbf', gamma='auto')
    score = make_scorer(accuracy_score)
    clf = cross_val_score(estimator=model,X=X_train,y=y_train,cv=3,scoring=score)
    accuracy = np.mean(clf)
    return (accuracy - 0.005 * X.shape[1] / tot)

#%%
X_all = load_breast_cancer().data

scalar = StandardScaler()
X_all = scalar.fit_transform(X_all)
y_all = load_breast_cancer().target

pop = np.random.randint(2, size=(8,X_all.shape[1]))

fit = pd.DataFrame(np.zeros((8,3)))

for k in range(100):
    for i in range(8):
        fit.iloc[i,0] = i
        fit.iloc[i,1] = bin2val(pop[i],-5,5,4)
        fit.iloc[i,2] = svm_cv(X_all, y_all, pop[i])
    
    fit_sort = (selection(fit, len(pop))).sort_values(by = 2, ascending=False)
    
    new_pop_sel = np.zeros_like(pop, dtype=int)
    for i in range(len(pop)):
        new_pop_sel[i] = pop[int(fit_sort.iloc[i,0])]
        
    new_pop_cross = crossover(new_pop_sel, len(pop), 4, 0.3)
    
    new_pop_mut = mutation(new_pop_cross, len(pop), 4, 0.125)
    
    pop = new_pop_mut

fit_sort.columns = ['SrNo','Value','Fitness']
print("Maximum accuracy obtained %f:"%fit_sort.iloc[0,2])
print("Number of features : %d"%len(np.where(new_pop_sel[0] == 1)[0]))
