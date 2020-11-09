import numpy as np
import matplotlib.pyplot as plt

class pedulum(object):
    def __init__(self, Fd, omega = 0,theta = 0.2 ):
        self.Fd = Fd
        self.t = [0]
        self.w = [omega]
        self.theta = [theta]
        self.wd = 2/3
        self.q = 0.5
        self.dt = 0.01
        self.g = 9.8
        self.l = 9.8
    
    def drive(self):
        while self.t[-1] < 6000:
            
            self.w.append(self.w[-1]-((self.g/self.l)*np.sin(self.theta[-1])+self.q*self.w[-1]-self.Fd*np.sin(self.wd*self.t[-1]))*self.dt)
            
            self.theta.append(self.theta[-1]+self.w[-1]*self.dt)
            
            if self.theta[-1]>np.pi:
                self.theta[-1] = self.theta[-1] - 2*np.pi    
            
            if self.theta[-1]<-np.pi:
                self.theta[-1] = self.theta[-1] + 2*np.pi
            
            self.t.append(self.t[-1]+self.dt)
            
           
    def plotw(self):
        plt.plot(self.theta,self.w)
        plt.show()
    
    def plot_wtheta(self):
        
        for i in range(0, len(self.t)):
            x = (self.wd*self.t[i]) /(2*np.pi)
            if abs(x - round(x)) < 0.001:
                plt.scatter(self.theta[i],self.w[i],color = 'blue')
        plt.xlabel("Theta(radians)")
        plt.ylabel("Omega(radians/s)")
        plt.title("Omega versus Theta F_D = {}".format(self.Fd))
        plt.show()

a = pedulum(1.2)
a.drive()
a.plot_wtheta()


