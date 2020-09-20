from vpython import *
from math import pi
import random
random.seed(None)
jmax = 1000
xx = yy =zz =0.0
graph1 = canvas(x=0, y=0, width=600, height = 600, title = '3D Random Walk', forward =vector(-0.6, -0.5, -10), background=color.white)
pts = curve(pos=(0,0,0),radius=10.0, color=color.yellow)
xax = curve(color = color.red, pos=[(0,0,0),(1500,0,0)],radius=10.)
yax = curve(color = color.red, pos=[(0,0,0),(0,1500,0)],radius=10.)
zax = curve(color = color.red, pos=[(0,0,0),(0,0,1500)],radius=10.)
xname = label(text = "X", pos = vector(1000, 150, 0),box=0)
yname = label(text = "Y", pos = vector(-100, 1000, 0),box=0)
zname = label(text = "Z", pos = vector(100, 0, 1000),box=0)
for i in range(1, 100):
    xx +=(random.random() - 0.5)*2
    yy +=(random.random() - 0.5)*2
    zz +=(random.random() - 0.5)*2
    pts.append(vector(200*xx - 100, 200*yy - 100, 200*zz - 100))
    rate(100)
print("This walk's distance R =", sqrt(xx*xx + yy*yy + zz*zz))