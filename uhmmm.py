from sympy import *
total_n, bins_n = symbols('prob total_n bins_n')
prob= (bins_n / total_n)



import numpy as np
from itertools import product

def fold(a):
    return np.tril((a*np.tri(a.shape[0],a.shape[1],-1))+a)
    
a=np.ones((3,3))
print a
f=fold(a)
print f


a=np.array([[1,2,1],[2,1,2],[3,2,3]],np.int)
print a
print fold(a)



def cartesian(l):
    return product(*(l,)*len(l))

def onlyholds(l):
    return sorted([sorted(p) for p in cartesian(l)])

for p in onlyholds(['X','Y']): print p


class Index():
    def __init__(self):
        self.keys = {}
        self.count = 0

    def __getitem__(self, k):
        if k not in self.keys:
            idx=count
            self.keys[k] = idx
            self.count += 1
            return idx
        return self.keys[k]

