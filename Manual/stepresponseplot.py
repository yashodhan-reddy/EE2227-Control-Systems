import numpy as np
import matplotlib.pyplot as plt

root3=np.sqrt(3)
t=np.linspace(0,100)
a=np.exp(-5*t)
b=np.cos(5*root3*t)
d=np.sin(5*root3*t)
C=(-((51/50)*b)-((17*root3/50)*d))*a+1.02

plt.figure()
plt.plot(t, C)
plt.xlabel('$t$')
plt.ylabel('$Step Response$')
plt.show()
