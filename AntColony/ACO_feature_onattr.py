#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:09:42 2019

@author: akshay.nadgire
"""

import numpy as np
import random
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC  
from sklearn.model_selection import cross_val_score

scaler = StandardScaler()
X = load_iris().data
X = scaler.fit_transform(X)
y = load_iris().target
phero = np.random.random((4))

#%%
for m in range(500):
    q0 = 0.7
    travel = np.zeros((4,3),dtype=int)
    
    startpt = np.random.randint(0,4,4)
    
    for i in range(len(startpt)):
        start = startpt[i]
        tmpPh = np.copy(phero)
        tmpPh[start] = 0
        travel[i,0] = start
        
        for j in range(1,3):
            q = random.random()
            if q <= q0:
                nxt = np.argmax(tmpPh)
                travel[i,j] = nxt
                tmpPh[nxt] = 0
            else:
                prob = list(tmpPh[:] / sum(tmpPh[:]))
                nxt = np.random.choice(range(4), p=prob)
                travel[i,j] = nxt
                tmpPh[nxt] = 0
            start = nxt
    #%%
    
    acc = np.zeros((4))
    
    for i in range(len(travel)):
        subset = list(travel[i,:])
        X1 = X[:,subset]
    
        model = SVC()
        scores = cross_val_score(model, X1, y, cv=3)
        acc[i] = np.mean(scores)
    #%%
    
    bestAttr = travel[np.argmax(acc),:]
    phero = phero * 0.9
    for i in bestAttr:    
        phero[i] = phero[i] * 1.2 / 0.9
#%%
print([0,1,2])
scores_all = cross_val_score(model, X[:,[2,3,0]], y, cv=3)
print(np.mean(scores_all))
