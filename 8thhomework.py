import numpy as np

# 第四象限
def update_V(V_old, V_new):
    for i in range(0, 20):
        for j in range(0, 20):
            if(i!=0  and j != 0 and j!=6):
                V_new[i, j] = 0.25 * (V_old[i + 1, j] + V_old[i - 1, j] + V_old[i, j + 1] + V_old[i, j - 1])
            elif(i!=0 and j == 0):
                V_new[i, j] = 0.25 * (V_old[i - 1, j] + V_old[i + 1, j] )
            elif(i == 0 and j!= 0 ):
                V_new[i, j] = 0.25*(V_old[i, j - 1]+V_old[i, j + 1])
                
            if (i<=10 and j==6):
                V_new[0:10,j] = V_old[0:10,j]
            if (i>= 10 and j ==6 ):   
                V_new[11:20,j] = 0.25 * (V_old[i + 1, j] + V_old[i - 1, j] + V_old[i, j + 1] + V_old[i, j - 1])
                
    return V_new

def cal_dV(V_old, V_new):
    dV = 0
    for i in range(0, 20):
        for j in range(0, 20):
            dV += np.abs(V_new[i, j] - V_old[i, j])
    return dV

V1 = np.zeros((21,21))
V2 = np.zeros((21,21))
V1[0:20,20]=0
V1[20,0:20]=0
V1[0:10,6]=1
V1[0:10,4]= 0.37
V1[0:5,8]= 0.63
V1[11,6] = 0.8
V1[13,6] = 0.7
V1[14,6] = 0.6

i=1
while(True):
    update_V(V1, V2)
    update_V(V2, V1)
    i += 1
    dV = cal_dV(V2, V1)
    if(i > 20):
        if(dV < 1e-1):
            break
            
from pylab import *
from mpl_toolkits.mplot3d import Axes3D

fig = figure()
ax = Axes3D(fig)

X = np.arange(0, 1.05, 0.05)
Y = np.arange(0, 1.05, 0.05)
X, Y = np.meshgrid(X, Y)
xlabel("X")
ylabel("Y")
ax.plot_surface(X,Y, V1,rstride=1, cstride=1)

show()

V_lt = np.zeros((21,21))
V_rt = np.zeros((21,21))
V_lb = np.zeros((21,21)) #lt repersents left-top, and rb represents right-bottom.

for i in range(21):
    for j in range(21):
        V_lt[i, j] = -V1[20 - i,20 - j]
        V_lb[i, j] = -V1[i, 20 - j]
        V_rt[i, j] = V1[20 - i, j]

V_l = np.concatenate((V_lt, V_lb))
V_r = np.concatenate((V_rt, V1))
V = np.concatenate((V_l, V_r), axis = 1)
        
fig1 = figure()
ax1 = Axes3D(fig1)

X = np.arange(-1.05, 1.05, 0.05)
Y = np.arange(-1.05, 1.05, 0.05)
X, Y = np.meshgrid(X, Y)
xlabel("X")
ylabel("Y")
ax1.plot_surface(X,Y,V,rstride=1, cstride=1)

show()
