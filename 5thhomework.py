import matplotlib.pyplot as plt
import numpy as np
from vpython import *

class knuckleball():
    def __init__(self, v, w, theta, alpha=0):  
        self.v = [v]
        self.w = w
       
        self.theta = [theta]
        self.x = [0]
        self.y = [1.7]
        self.z = [0]
        self.vx = [v*np.cos(alpha*np.pi/180)]
        self.vy = [v*np.sin(alpha*np.pi/180)]
        self.vz = [0]
        self.g = 9.8
        self.dt = 0.01
        

    def B2_m(self):
        return 0.0039+0.0058/(1+np.exp((self.v[-1] - 35)/5))
    def f_drag_x(self):
        return -self.B2_m()*self.v[-1]*self.vx[-1]
    def f_drag_y(self):
        return -self.B2_m()*self.v[-1]*self.vy[-1]
    def f_drag_z(self):
        return -self.B2_m()*self.v[-1]*self.vz[-1]
    def f_magnus(self):
        return -4.1*10**(-4)*self.w*self.vx[-1]
    def f_lateral(self):
        return self.g*0.5*(np.sin(4 * self.theta[-1] * np.pi / 180) - 0.25 * np.sin(8 * self.theta[-1] * np.pi / 180\
        + 0.08 * np.sin(12 * self.theta[-1] * np.pi / 180) - 0.025 * np.sin(16 * self.theta[-1] * np.pi / 180)))
    def pitch(self):
        while(self.x[-1]<18 and self.y[-1]>0):
            self.x.append(self.x[-1] + self.vx[-1] * self.dt)
            self.y.append(self.y[-1] + self.vy[-1] * self.dt)
            self.z.append(self.z[-1] + self.vz[-1] * self.dt)
            self.vx.append(self.vx[-1]+self.f_drag_x()*self.dt)
            self.vy.append(self.vy[-1]+(-self.f_drag_y()-self.g)*self.dt)
            self.vz.append(self.vz[-1]+(self.f_drag_z()+self.f_magnus()+self.f_lateral())*self.dt)
            self.theta.append(self.theta[-1] + self.w* self.dt)
            self.v.append(np.sqrt(self.vx[-1] ** 2 + self.vy[-1] ** 2 + self.vy[-1] ** 2))
    def plot_xy(self):
        plt.plot(self.x,self.y,label = "α={}°".format(i))
        plt.title("Knuckleball (x-y)")
        plt.xlabel("x/m")
        plt.ylabel("y/m")
        plt.legend()
        plt.grid()
        #plt.show()
    def plot_xz(self):
        plt.plot(self.x, self.z,label = "α={:.1f}°".format(i))
        plt.title("Knuckleball (x-z)")
        plt.xlabel("x/m")
        plt.ylabel("z/m")
        plt.legend()
        plt.grid()
        #plt.show()
    def plot3D(self):
        scene.center=vector(0,0,0)
        baseball = sphere(pos=vector(0,1.7,0),radius=0.02,color=color.green,make_trail=True)
        baseball.v = vector(self.vx[-1],self.vy[-1],self.vz[-1])
        box(pos = vector(50,0,0),size = vector(10,0.1,5),color=color.yellow) 
        while baseball.pos.y>0.0001 and baseball.pos.x<18:
            rate(400)
            a = vector(self.f_drag_x(),self.f_drag_y()-self.g,self.f_drag_z()+self.f_magnus()+self.f_lateral())
            baseball.v = baseball.v+a*self.dt
            baseball.pos = baseball.pos + baseball.v*self.dt




for i in np.arange(0,50,5):
    ball= knuckleball(30,0.35*360,0,i)
    ball.pitch()
    ball.plot_xy()
plt.show()
for i in np.arange(45,95,5):
    ball= knuckleball(30,0.35*360,0,i)
    ball.pitch()
    ball.plot_xy()
plt.show()



