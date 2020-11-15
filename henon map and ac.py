# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 09:06:05 2020

@author: Charlie
"""
import numpy as np
import matplotlib.pyplot as plt

#henon chaotic map
numsteps=1000

x=np.empty(numsteps+1)
y=np.empty(numsteps+1)

x[0]=0.1
y[0]=0.28

a=1.4
b=0.3

'''for i in range(numsteps):
    x[i+1]=1-(a*(x[i]**2))+y[i]
    y[i+1]=b*x[i]'''

x1=np.empty(numsteps+1)
y1=np.empty(numsteps+1)

x1[0]=0.100000001, y1[0]=0.28, a=1.4, b=0.3

for i in range(numsteps):
    x1[i+1]=1-(a*(x1[i]**2))+y1[i]
    y1[i+1]=b*x1[i]
    
    
n=range(numsteps+1)
#plt.plot(n,x1)
#print(k)

#plt.plot(n,y)

#acx=np.correlate(x,x,mode='full')
#acy=np.correlate(y,y,mode='full')
#plt.plot(n, x)
#plt.plot(n, y)

#print(x,y)
'''2d x v y
plt.xlabel("Number of Iterations")
plt.ylabel("x,y")
plt.plot(n, x, label='x')
plt.plot(n, y, label='y')
plt.legend()'''

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot(x1, y1, n, lw=0.3)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
#ax.set_title("Henon Map")

plt.show()

'''#2d x1 x 
plt.xlabel("Number of Iterations")
plt.ylabel("x")
plt.plot(n, x, label='x0=0.1')
plt.plot(n, x1, label='x0=0.100000001')
plt.legend()'''
