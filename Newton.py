from matplotlib import pyplot as plt
import time
from scipy.misc import derivative
from Bi import c_w

def newton_iter(x0,tol,func):
    plt.xlabel("k")
    plt.ylabel("c_w(f)")
    plt.title("Fig7: Newton Method k-c_w(f) image")
    start = time.time()
    x1 = x0 - func(x0)/derivative(func,x0,10**(-8))
    xs = [c_w(x1)]
    k = 1
    ks = [k]
    while abs(x0-x1)>=tol:
        x0 = x1
        x1 = x0-func(x0)/derivative(func,x0,10**(-8))
        k+=1
        ks.append(k)
        xs.append(c_w(x1))
    print("Run time is:",time.time()-start)
    plt.plot(ks, xs)
    plt.plot(ks, [0]*len(ks))
    plt.show()
    return x1,k

newton_iter(0.00001, 10**(-15),c_w)