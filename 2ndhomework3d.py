import numpy as np
import matplotlib.pyplot as plt

ns = []
differences = []
for n in range(1, 10001):
    Sdn_Kahan = Sdn = c = np.float(0)
    for i in range(1, n+1):
        Sdn = np.float(1/(n+1-i) + Sdn)
        y = np.float(1/(n+1-i) -c)
        t = np.float(Sdn_Kahan + y)
        c = np.float(t - Sdn_Kahan - y)
        Sdn_Kahan = t
    difference = abs(Sdn_Kahan - Sdn)
    
    ns.append(n)
    differences.append(difference)
plt.plot(ns, differences)
plt.title("The Differences between Sdn_Kahan and Sdn" )
plt.show()


