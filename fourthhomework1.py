import math
pi = math.pi
class Komplex:
    def __init__(self,x,y,typec=0):
        if typec == 0:
            self.re = x #typec为0：直角坐标系
            self.im = y
        else:
            self.re=x*math.cos(y)
            self.im=x*math.sin(y) #否则极坐标系
        self.typec=typec
   
     
   
    def getRe(self):
        return self.re
    
    def getIm(self):
        return self.im
    
    def getMod(self):
        return math.sqrt(self.re**2+self.im**2)
    
    def getTheta(self):
        if self.re == 0:
            if self.im > 0:
                return pi/2
            elif self.im == 0:
                return 0
            else:
                return -pi/2
        else:
            return math.atan(self.im/self.re)
   
    def __add__(self,other):
        return Komplex(self.re + other.re,self.im + other.im)
    
    def __sub__(self,other):
        return Komplex(self.re - other.re , self.im - other.im)
    
    def __mul__(self,other):
        return Komplex(self.re*other.re - self.im*other.im , self.re*other.im + self.im*other.re)
    
    def __truediv__(self,other):
        numre = self.re * other.re + self.im*other.im
        deno = other.re *other.re + other.im*other .im 
        numim = self .im *other.re - self.re*other .im
        return Komplex(numre/deno , numim/deno) 
    
    def conj(self):
        return Komplex(self.re , - self.im)
    
    def set_typec(self): #改变表达形式
        if self.typec == 0:
           self.typec = 1
        else:
            self.typec = 0
        return self
    
    def __repr__(self):
        if self.typec== 0:
            return '直角坐标系：(%f,%f)'  %(self.re,self.im)
        else:
            return '极坐标：(%f,%f)'  %(self.getMod(),self.getTheta()) 
