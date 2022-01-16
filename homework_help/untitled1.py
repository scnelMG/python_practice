# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 19:58:20 2021

@author: Mgyu
"""
num=int(input())
​def prime(a):
    if a<2:
        return False
    elif a==2:
        return True
    else:
        for i in range(2,a):
            if a%i==0:
                retrun False
            return True
        
for i in range(1, num+1):
    if prime(i):
        print(i, end="" )