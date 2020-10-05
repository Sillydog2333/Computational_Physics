import numpy as np
import time
N = 1000000 
start_time1 = time.time()
Sup = np.float32(0)
Sdn = np.float32(0)

for i in range(1,N+1):
    Sup = np.float32(1/i + Sup)
    Sdn = np.float32(1/(N+1-i) + Sdn)
end_time1 = time.time() #用for循环计算消耗的时间


start_time2 = time.time()
s1 = np.arange(1,N+1,dtype=np.float32)#产生[1，2，...N]单精度浮点数队列
s2 = np.arange(N,0,-1,dtype = np.float32)#产生[N,N-1,...1]单精度浮点数队列
s_up = 1/s1
s_up_sum = s_up.sum()
s_down = 1/s2
s_down_sum = s_down.sum()
end_time2 = time.time()

total_time1 = end_time1 - start_time1
total_time2 = end_time2 - start_time2

print("total_time1 = ",total_time1)
print("total_time2 = ",total_time2)
print("Sup = ",Sup)
print("s_up_sum = ",s_up_sum)
print("Sdn = ",Sdn)
print("s_down_sum = ", s_down_sum)