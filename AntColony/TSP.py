#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 14:15:31 2019

@author: akshay.nadgire
"""

import numpy as np
import random

city = 4
ant = 4

di = np.diag_indices(city)

pheromene = np.random.random(size=(city,city))
pheromene = (pheromene + pheromene.T) / 2
pheromene[di] = 0

distance = np.random.randint(10,100,size=(city,city))
distance = (distance + distance.T) / 2
distance[di] = 0

phero = pheromene
dist = distance
            
#%%
phcl = phero / dist
phcl[di] = 0
       
start = np.random.randint(4,size=(4))

travel = np.zeros((4,5), dtype=int)
q0 = 0.6

for i in range(4):
    travel[i,0] = start[i]
    travel[i,-1] = start[i]
    tmpPC = np.copy(phcl)
    ss = start[i]
    tmpPC[:,ss] = 0
    for j in range(1,4):
        q = random.random()
        if q <= q0: 
            nxt = np.argmax(tmpPC[ss,:])
            travel[i,j] = nxt
            tmpPC[:,nxt] = 0
        else:
            prob = list(tmpPC[ss,:] / sum(tmpPC[ss,:]))
            nxt = np.random.choice(range(4), p=prob)
            travel[i,j] = nxt
            tmpPC[:,nxt] = 0
        ss = nxt

totaldist = np.zeros((4))
for i in range(4):
    tmpD = 0
    for j in range(4):
        tmpD = tmpD + dist[travel[i,j], travel[i,j+1]]
    totaldist[i] = tmpD
    
#minDistInx = np.where(min(totaldist) == totaldist)[0]
mDinx = np.argmin(totaldist)

phero = phero * 0.8

for i in range(4):
    phero[travel[mDinx, i], travel[mDinx, i+1]] = phero[travel[mDinx, i], travel[mDinx, i+1]] * 1.2/0.8

#%%
