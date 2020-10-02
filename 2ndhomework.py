import numpy as np
import matplotlib.pyplot as plt
x = 1 #给定初始值
tol = np.float(10**-8)
taylor_sinx = np.float(x) #级数解
sinx = np.float(np.sin(x)) #sin(x)准确值
xs = []
sinxs = []
taylor_sinxs = [] #准备数据画图
while abs(sinx - taylor_sinx) <= 5: #为了明显看到发散设置为5
    n = 1
    term = np.float(x) 
    taylor_sinx = np.float(x)
    sinx =np.float(np.sin(x))
    while abs(term/taylor_sinx)>=tol:
        n = n + 1
        term = np.float(-term*x*x/((2*n-1)*(2*n -2)))
        taylor_sinx = np.float(taylor_sinx + term) #求出x所在位置的近似级数解
    
    xs.append(x)
    sinxs.append(sinx)
    taylor_sinxs.append(taylor_sinx)#往画图的列表中添加元素
    x = np.float(x + 0.01) #这里可以调绘制散点图的步长和解的精确度
print("x=",x)
print("sin(x)=",sinx)
print("taylor_sinx=", taylor_sinx)
plt.scatter(xs,taylor_sinxs,c='blue')
plt.title("A Scatter Plot of the Talor-Series Solution to sin(x) ")
plt.show()