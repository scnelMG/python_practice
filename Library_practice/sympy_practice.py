# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 00:45:51 2021

@author: 박민규
"""
import sympy as sy
x = sy.symbols('x')
expr = 2*x
expr.subs(x,2)

# differnetialtion 미분
f = x**3
df1 = sy.diff(f,x)
df2 = sy.diff(df1,x)
df3 = sy.diff(df2,x)
f= sy.sin(x)
df1 = sy.diff(f,x)

# integrate 적분
sy.integrate(f,(x,0,3.14))
sy.integrate(f,(x,0,2*sy.pi))

# limit
sy.limit(sy.sin(x)/x,x,0)

# ex_선미분 방정식
t = sy.symbols('t')
x = sy.Function('x')
ODE = sy.Eq(sy.diff(x(t),t,t) + x(t))
sy.dsolve(ODE,x(t))















