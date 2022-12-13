import imp
from matplotlib import pyplot as plt
import numpy as np
from Bi import c_w

x = np.arange(0.0001,0.2,0.0001)
y = [c_w(i) for i in x]
y_0 = np.zeros(x.shape)
plt.plot(x,y)
plt.plot(x, y_0)
plt.xlabel("f")
plt.ylabel("f(y)")
plt.title("Fig 1: Image of function")
plt.show()