import numpy as np
import matplotlib.pyplot as plt 

class three_body():
    def __init__(self, n, mE=6*10**24,mJ = 1.9*10**27,mS = 2*10**30,T_E=1,T_J=11.86,rE0=0.095,rJ0=-5.195,rS0=-0.005,totaltime=20):
        
        self.m_E= mE
        self.m_J= n*mJ
        self.m_S= mS

        self.r_EJ = []
        self.r_ES = []
        self.r_SJ = []

        self.x_E = [rE0]
        self.y_E = [0]
        self.x_J = [rJ0]
        self.y_J = [0]
        self.x_S = [rS0]
        self.y_S = [0]

        self.vE_x = [0]
        self.vE_y = [(2*np.pi*rE0)/T_E]
        self.vJ_x = [0]
        self.vJ_y = [(2*np.pi*rJ0)/T_J]
        self.vS_x = [0]
        self.vS_y = [(-1/self.m_S)*(self.m_E*(2*np.pi*rE0)/(T_E) + self.m_J*(2*np.pi*rJ0)/(T_J))]

        self.dt = 0.001
        self.t = [0]
        self.t_tot = totaltime

        self.T = []
    
    def motion(self):
        while self.t[-1] < self.t_tot:
            self.r_EJ.append(np.sqrt( (self.x_J[-1]-self.x_E[-1])**2+(self.y_J[-1]-self.y_E[-1])**2 ))
            self.r_ES.append(np.sqrt( (self.x_S[-1]-self.x_E[-1])**2+(self.y_S[-1]-self.y_E[-1])**2 ))
            self.r_SJ.append(np.sqrt( (self.x_S[-1]-self.x_J[-1])**2+(self.y_S[-1]-self.y_J[-1])**2 )) 

            
            self.vE_x.append(self.vE_x[-1]-(4*np.pi**2*(self.x_E[-1]-self.x_S[-1])/self.r_ES[-1]**3)*self.dt-(4*np.pi**2*(self.m_J/self.m_S)\
            *(self.x_E[-1]-self.x_J[-1]))/self.r_EJ[-1]**3*self.dt)
            
            self.vE_y.append(self.vE_y[-1]-(4*np.pi**2*(self.y_E[-1]-self.y_S[-1])/self.r_ES[-1]**3)*self.dt-(4*np.pi**2*(self.m_J/self.m_S)\
            *(self.y_E[-1]-self.y_J[-1]))/self.r_EJ[-1]**3*self.dt)
            
            self.vJ_x.append(self.vJ_x[-1]-(4*np.pi**2*(self.x_J[-1]-self.x_S[-1])/self.r_SJ[-1]**3)*self.dt-(4*np.pi**2*(self.m_E/self.m_S)\
            *(self.x_J[-1]-self.x_E[-1]))/self.r_EJ[-1]**3*self.dt)

            self.vJ_y.append(self.vJ_y[-1]-(4*np.pi**2*(self.y_J[-1]-self.y_S[-1])/self.r_SJ[-1]**3)*self.dt-(4*np.pi**2*(self.m_E/self.m_S)\
            *(self.y_J[-1]-self.y_E[-1]))/self.r_EJ[-1]**3*self.dt)

            self.vS_x.append(self.vS_x[-1]+(4*np.pi**2*(self.x_E[-1]-self.x_S[-1])/self.r_ES[-1]**3)*self.dt+(4*np.pi**2*(self.x_J[-1]-self.x_S[-1])/self.r_SJ[-1]**3)*self.dt)
            
            self.vS_y.append(self.vS_y[-1]+(4*np.pi**2*(self.y_E[-1]-self.y_S[-1])/self.r_ES[-1]**3)*self.dt+(4*np.pi**2*(self.y_J[-1]-self.y_S[-1])/self.r_SJ[-1]**3)*self.dt)

            self.x_E.append( self.x_E[-1] + self.vE_x[-1] * self.dt )
            self.y_E.append( self.y_E[-1] + self.vE_y[-1] * self.dt )
            self.x_J.append( self.x_J[-1] + self.vJ_x[-1] * self.dt )
            self.y_J.append( self.y_J[-1] + self.vJ_y[-1] * self.dt )
            self.x_S.append( self.x_S[-1] + self.vS_x[-1] * self.dt )
            self.y_S.append( self.y_S[-1] + self.vS_y[-1] * self.dt )

            self.T.append(288.15*( (1/self.r_EJ[-1])**2 + (1/self.r_ES[-1])**2 )-273.15 )

            self.t.append(self.t[-1]+self.dt)

    def three_body_plot(self):
        plt.plot(self.x_E,self.y_E,color='blue' )
        plt.plot(self.x_J,self.y_J,color='yellow')
        plt.plot(self.x_S,self.y_S,color='red')
        plt.xlabel("x (AU)")
        plt.ylabel("y (AU)")
        #plt.title("3-body motion simulation, MJ= {:.0f}mJ ".format((self.m_J/1.9/10**27)) )
        plt.show()



a = three_body(1)
a.motion()
a.three_body_plot()



