# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 01:44:03 2020

@author: DineshBabu
"""


#Question 1  
from scipy import integrate
from scipy.integrate import nquad
def f(x, y): return np.exp((-x)-y)
integrate.nquad(f, [[0, np.inf],[0, np.inf]])
