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

def Reset():
    globals().pop('extent')
    globals().pop('ax')


if 'extent' not in locals():
    extent = [-5,5,-5,5]
elif 'ax' in locals():
    try:
        extent = list(ax.get_xlim()) + list(ax.get_ylim())
    except NameError:
        pass

resolution = 500
numIter = 50

def Iteration(Z,I,n,f):
    Z.flat[I] = f(Z.flat[I])
    escaped = np.abs(Z.flat[I]) > 200
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
        I = Iteration(Z,I,i,f2)

plt.figure()
ax = plt.axes()
plt.imshow(N,interpolation='none',extent=extent,origin='lower')

#def on_xlims_change(axes):
#    print ("updated xlims: ", axes.get_xlim())

def on_ylims_change(axes):
    print ("updated xlims: ", axes.get_xlim())
    print ("updated ylims: ", axes.get_ylim())

#ax.callbacks.connect('xlim_changed', on_xlims_change)
ax.callbacks.connect('ylim_changed', on_ylims_change)

