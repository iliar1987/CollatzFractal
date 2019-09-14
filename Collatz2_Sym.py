# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 07:40:48 2019

@author: IliaRaysin
"""

from sympy import solve,Symbol,I
from sympy.abc import a,b,c,d,g,h,n
import sympy

def Sf1(p,n):
    return sum(p[i] * (1-sympy.cos(2*sympy.pi/3 * (n+i)))*2/3 for i in range(3))

def Sf2(p,n):
    return sum(p[i] * (sympy.exp(sympy.I * 2*sympy.pi/3 * n*(i+1)))*2/3 for i in range(3))

Sf = Sf2

Eqs = [3*Sf([a,b,c],0)-2,3*Sf([a,b,c],1)-4,3*Sf([a,b,c],2)-4,
       3*Sf([d,g,h],0),3*Sf([d,g,h],1)+1,3*Sf([d,g,h],2)-1]
print(Eqs)
sol = solve(Eqs)
print(sol)

F1 = Sf1([a*n+d,b*n+g,c*n+h],n).subs(sol)
F2 = Sf2([a*n+d,b*n+g,c*n+h],n).subs(sol)
print(sympy.simplify(F1))
print(F2)
complex(F2.subs(n,2))

import numpy as np
from numpy.linalg import det
N = np.array([[0,1,2],[1,2,0],[2,0,1]])
A = (1-np.cos(2*np.pi/3 * N))*2/3
print(np.linalg.det(A))
B = (1-np.exp(1j*2*np.pi/3 * N))*2/3
print(np.linalg.det(B))
C = (1-np.cos(2*np.pi/3 * N))*2/3
#C = np.concatenate((C,np.ones((3,1))),axis=1)
print(np.linalg.matrix_rank(C))
print(det(C))
