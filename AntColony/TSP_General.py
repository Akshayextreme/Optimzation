#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 14:15:31 2019

@author: akshay.nadgire
"""

import numpy as np
import random
            
#%%
def Antpath(phcl, start, C, A):
    travel = np.zeros((A,C+1), dtype=int)
    q0 = 0.6
    
    for i in range(A):
        travel[i,0] = start[i]
        travel[i,-1] = start[i]
        tmpPC = np.copy(phcl)
        ss = start[i]
        tmpPC[:,ss] = 0
        for j in range(1,C):
            q = random.random()
            if q <= q0: 
                nxt = np.argmax(tmpPC[ss,:])
                travel[i,j] = nxt
                tmpPC[:,nxt] = 0
            else:
                prob = list(tmpPC[ss,:] / sum(tmpPC[ss,:]))
                nxt = np.random.choice(range(C), p=prob)
                travel[i,j] = nxt
                tmpPC[:,nxt] = 0
            ss = nxt
    return travel

#%%
def DistCal(dist, travel, C, A):
    totaldist = np.zeros((A))
    for i in range(A):
        tmpD = 0
        for j in range(C):
            tmpD = tmpD + dist[travel[i,j], travel[i,j+1]]
        totaldist[i] = tmpD
    return totaldist

#%%
def TSP(dist, phero, C, A):
    
    phcl = phero / dist
    di = np.diag_indices(C)
    phcl[di] = 0
           
    start = np.random.randint(C,size=(A))
    
    travel = Antpath(phcl, start, C, A)
    
    totaldist = DistCal(dist, travel, C, A)  
    
    #minDistInx = np.where(min(totaldist) == totaldist)[0]
    mDinx = np.argmin(totaldist)
    
    phero = phero * 0.8
    
    for i in range(C):
        phero[travel[mDinx, i], travel[mDinx, i+1]] = phero[travel[mDinx, i], travel[mDinx, i+1]] * 1.2/0.8
        
    return phero

#%%
city = 6
ant = 6

di = np.diag_indices(city)

pheromene = np.random.random(size=(city,city))
pheromene = (pheromene + pheromene.T) / 2
pheromene[di] = 0

distance = np.random.randint(10,100,size=(city,city))
distance = (distance + distance.T) / 2
distance[di] = 0
#%%

for l in range(100):
    pheromene = TSP(distance, pheromene, city, ant)
    
FinalTravel = Antpath(pheromene, [0, 1, 2, 3, 0, 1], city, ant)

FinalDistance = DistCal(distance, FinalTravel, city, ant)

ShortestPath = FinalTravel[np.argmin(FinalDistance)]

print(ShortestPath)
print(min(FinalDistance))