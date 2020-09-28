# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 01:44:38 2020

@author: DineshBabu
"""

#Question 2:

from itertools import combinations 

def findPairs(lst, k): 
	return [(x, y) for x, y in combinations(lst, r = 2) 
				if abs(x - y) == k] 
lst = [1, 3, 5] 
k = 2
print(findPairs(lst, k))     