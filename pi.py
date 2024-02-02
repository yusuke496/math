import matplotlib.pyplot as plt
import numpy as np
import random
n=100000000
n2=1000000
x=np.array([i for i in range(0,int(n/n2))])
y=np.array([0.0 for i in range(0,int(n/n2))])
y2=np.array([0.0 for i in range(0,int(n/n2))])
p=1
for i in range(1,n+1) :
    p=p+(-1)**i*1/(2*i+1)
    if i % n2 == 0 :
        y[int(i//n2)-1]=4*p
        print(i, "\t", y[int(i//n2)-1])

i=0
l=0
for i in range(1,n+1) :
    xr=random.random()
    yr=random.random()
    if xr**2+yr**2 < 1 :
        l=l+1
    else :
        l=l
    if i % n2 == 0 :
        y2[int(i//n2)-1]=4*l/i
        print(i, "\t", y2[int(i//n2)-1])

plt.plot(x,y)
plt.plot(x,y2)
plt.ylim(3.140,3.144)
plt.show()

