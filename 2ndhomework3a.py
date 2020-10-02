 #2a
import numpy as np
N = input("Please input N")
N = int(N)
Sup = np.float(0)
Sdn = np.float(0)

for i in range(1,N+1):
    Sup = np.float(1/i + Sup)
    Sdn = np.float(1/(N+1-i) + Sdn)

print("S^{(up)}=",Sup)
print("S^{(down)}",Sdn)
