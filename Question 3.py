# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 01:45:05 2020

@author: DineshBabu
"""

#Question 3

data = [("username1", "phone_number1", "email1"),
        ("usernameX", "phone_number1", "emailX"),
        ("usernameZ", "phone_numberZ", "email1Z"),
        ("usernameY", "phone_numberY", "emailX")]


def match(t1, t2):
    if (t1[0] == t2[0] or t1[1] == t2[1] or t1[2] == t2[2]):
        return True
    else:
        return False

together = []
for i in range(len(data)):
    temp = {i}
    for j in range(len(data)):
        if (match(data[i], data[j])):
            temp.add(j)
    together.append(temp)
for i in range(len(data)):
    ans = together[i]
    for j in range(i + 1, len(data)):
        if (bool(ans.intersection(together[j]))):
            ans = ans.union(together[j])
    print(ans)
