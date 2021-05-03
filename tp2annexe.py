# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 11:34:41 2021

Stockage
"""

import math as m

def g11(x):
    return (-3*x+9)**(1/4)
def g12(x):
    return -(-3*x+9)**(1/4)
def g2(x):
    return (m.acos(x)+2)/3
def g3(x):
    return m.log(7)-m.log(x)
def g41(x):
    return m.log(10+x)
def g42(x):
    return m.exp(x)-10
def g5(x):
    return m.atan((x+5)/2)
def g6(x):
    return m.log((x**2)+3)
def g7(x):
    return (7-4*m.log(x))/3 
def g8(x):
    return (17+2*x**2-4*x)**(1/4)
def g9(x):
    return m.log(7+2*m.sin(x))
def g10(x):
    return m.log(10/m.log(x**2+4))