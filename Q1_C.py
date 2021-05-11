# -*- coding: utf-8 -*-
"""
Created on Sun May  9 09:27:12 2021

@author: Raza_Jutt
"""


import random

rand_x = []
rand_y = []
rand_z = []
for i in range(0,1000000):
    rand_x.append(random.uniform(0.00,1.00))
    rand_y.append(random.uniform(0.00,1.00))
    rand_z.append(random.uniform(0.00,1.00))


count = 0
for i in range(0,1000000):
    x=rand_x[i]
    y=rand_y[i]
    z=rand_z[i]
    if (pow(x,2)+pow(y,2)+pow(z,2)) <= 1.00:
        count = count + 1

print(count/1000000)
        
x = []
y = []
z = []
for i in range(0,101):
    for j in range(0,101):
        for k in range(0,101):
            if (pow(i/100,2)+pow(j/100,2)+pow(k/100,2)) <= 1.00:
                x.append(i/100)
                y.append(j/100)
                z.append(k/100)

# importing mplot3d toolkits, numpy and matplotlib
import numpy as np
import matplotlib.pyplot as plt
  
fig = plt.figure()
  
# syntax for 3-D projection
ax = plt.axes(projection ='3d')
  
# defining all 3 axes
x = np.array(x)
y = np.array(y)
z = np.array(z)

# plotting
ax.plot3D(x, y, z, 'blue')
ax.set_title('Sphare 3D 0 to 1 ')
plt.show()