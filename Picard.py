import math
from matplotlib import pyplot as plt
import time
from Bi import c_w

# Picard迭代法所用的迭代格式
def c_w_p(f,eps=0.00002,d=0.6,re=5813924.33689002):
    tmp = 2*math.log10( eps/(3.7*d)+2.51/( re*math.sqrt(f)) )
    return (1/tmp)**2

# Picard迭代法， x0为迭代起点，tol为精度，func为迭代格式
def picard(x0,tol,func):
    start = time.time()
    x1 = func(x0)
    xs = [x0,x1]
    k = 1
    ks = [0,k]
    while abs(x0-x1)>tol:
        x2 = func(x1)
        x0 = x1
        x1 = x2
        k+=1
        # 记录迭代过程
        ks.append(k)
        xs.append(x1)
    # 输出迭代时间
    print("Run time is:", time.time()-start)
    # 作图
    ys = [c_w(i) for i in xs]
    plt.plot(ks,ys)
    plt.show()
    return k, x1

# Run
# picard(0.00001, 10**(-15),c_w_p)