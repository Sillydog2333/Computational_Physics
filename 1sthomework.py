from vpython import *
import matplotlib.pyplot as plt
import random
import math
random.seed(None)
Rs=[]
for j in range(1,1001):
 xx = yy =zz =0.0
 for i in range(1, 100):
    xx +=(random.random() - 0.5)*2
    yy +=(random.random() - 0.5)*2
    zz +=(random.random() - 0.5)*2
    R=(sqrt(xx*xx + yy*yy + zz*zz))
 Rs.append(R)
print(Rs)
a = math.ceil(min(Rs))
b = math.floor(max(Rs))
print("a=",a)
print("b=",b)
plt.hist(Rs,bins=range(a,b,1))
plt.title("The Frequency Distribution of 3D Random Walking")
plt.show()