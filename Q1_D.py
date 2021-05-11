# -*- coding: utf-8 -*-
"""
Created on Sun May  9 19:49:48 2021

@author: Raza_Jutt
"""

import math
import random
import matplotlib.pyplot as plt
import numpy as np

x = []
for i in range(0,801):
    x.append(i/100)
    
y=[]
for i in x:
    y.append((-math.cos(0)/2) + (math.cos(i*i)/2))
    
rand_x = []
rand_y = []
for i in range(0,1000000):
    rand_x.append(random.uniform(0.00,8.00))
    rand_y.append(random.uniform(-1.00,0.00))
    
xpoints = np.array(x)
ypoints = np.array(y)

x_coordinates = rand_x
y_coordinates = rand_y

plt.plot(xpoints, ypoints,'r')
plt.scatter(x_coordinates, y_coordinates,s=0.1, marker="x")


plt.show()

count = 0
for i in range(0,1000000):
    x=rand_x[i]
    if (-math.cos(0)/2) + (math.cos(x*x)/2) > rand_y[i] :
        count += 1

print(count/1000000)

