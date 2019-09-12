# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 22:27:54 2019

@author: IliaRaysin
"""

import numpy as np
from matplotlib import pyplot as plt

def f1(z):
    return 0.25*((7*z + 2) - (5*z+2) * np.cos(z*np.pi))

def f2(z):
    return 0.25*((7*z + 2) - (5*z+2) * np.exp(1j*np.pi * z))

extent = [-5,5,-5,5]
resolution = 500
escapeRange = 200
numIter=100

def Iteration(N,Z,I,n,f):
    Z.flat[I] = f(Z.flat[I])
    escaped = np.abs(Z.flat[I]) > escapeRange
    N.flat[I[escaped]] = n
    return I[np.logical_not(escaped)]

def Run(numIter):
    x = np.linspace(extent[0],extent[1],resolution)
    y = np.linspace(extent[2],extent[3],resolution)
    X,Y = np.meshgrid(x,y)
    Z = X+1j*Y
    I = np.arange(len(Z.flat))
    N = np.ones(Z.shape) * np.nan
    for i in range(numIter):
        I = Iteration(N,Z,I,i,f2)
    return x,y,N

def DrawIntegers():
    if (extent[2] > 0) == (extent[3]>0):
        return
    a = np.arange(int(np.ceil(extent[0])),int(np.ceil(extent[1])))
    ax.plot(a,np.zeros(a.shape),'om')

x,y,N = Run(numIter)
plt.figure()
ax = plt.axes()
ax.imshow(N,interpolation='none',extent=extent,origin='lower')
DrawIntegers()

#def on_xlims_change(axes):
#    print ("updated xlims: ", axes.get_xlim())

def on_ylims_change(axes):
    global extent
#    print ("updated xlims: ", axes.get_xlim())
#    print ("updated ylims: ", axes.get_ylim())
    extent = list(axes.get_xlim()) + list(axes.get_ylim())
    x,y,N = Run(numIter)
    ax.clear()
    ax.callbacks.disconnect('ylim_changed')
    ax.imshow(N,interpolation='none',extent=extent,origin='lower')
    DrawIntegers()
    ax.callbacks.connect('ylim_changed', on_ylims_change)

#ax.callbacks.connect('xlim_changed', on_xlims_change)
ax.callbacks.connect('ylim_changed', on_ylims_change)



