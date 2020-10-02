import numpy as np
import matplotlib.pyplot as plt

ns = []
errs = []
for n in range(1, 100000001):
    Sup = Sdn = np.float(0)
    for i in range(1, n+1):
         Sup = np.float(1/i + Sup)
         Sdn = np.float(1/(n+1-i) + Sdn)
    err = np.float((Sup-Sdn)/(abs(Sup)+abs(Sdn)))
    ns.append(n)
    errs.append(err)
plt.loglog(ns, errs)
plt.title("Log-log Plot of ($S^{(up)}$-$S^{(down)}$)/($|S^{(up)}|$+$|S^{(down)}|$)")
plt.show()


