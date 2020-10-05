import numpy as np
import math
import matplotlib.pyplot as plt
pi = math.pi

#定义sin和cos的级数解法
def taylorsin(x):
    n = 1
    taylor_sinx = x 
    term = x
    while abs(term/taylor_sinx) >= 10**-10:
         n = n + 1
         term = -term*x*x/((2*n-1)*(2*n -2))
         taylor_sinx = taylor_sinx + term
    return taylor_sinx
def taylorcos(x):
    n = 1
    term = 1
    taylor_cosx = 1
    while abs(term/taylor_cosx) >= 10**-10:
         n = n + 1
         term = -term*x*x/((2*n-2)*(2*n -3))
         taylor_cosx = taylor_cosx + term 
    return(taylor_cosx)
def mysin(x):
    k = math.floor(x/pi)#若k为偶数，函数值为正，否则为负

    t = abs(x - k*pi -0.5*pi)#映射到0<x<pi的区间
    if k%2 == 0 :#判断k的奇偶性
        if  t <= pi*0.25:
            sinx = taylorcos(t)#离0.5*pi近，用cosx，否则为sinx
        else:
            sinx = taylorsin(0.5*pi-t)
    else:
        if  t <= pi*0.25:
            sinx = -taylorcos(t)
        else:
            sinx = -taylorsin(0.5*pi-t)
    return sinx
