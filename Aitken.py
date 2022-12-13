import time
from matplotlib import pyplot as plt
from Picard import c_w
from Picard import c_w_p

# x0: 起始位置; tol: 最小误差; func: 迭代函数
def Aitken_l(x0, tol,func):
    start = time.time()
    x1 = func(x0)
    x2 = func(x1)
    x3 = x2 - (x2-x1)**2/(x2-2*x1+x0)
    k = 1
    ys = [c_w(x3)]
    ks = [k]
    while abs(x3-x0)>=tol:
        x0 = x3
        x1 = func(x0)
        x2 = func(x1)

        # 防止除0错误
        if x2-2*x1+x0 == 0:
            print("run time is:", time.time()-start)
            plt.plot(ks,ys)
            plt.show()
            return x3,k
        
        x3 = x2 - (x2-x1)**2/(x2-2*x1+x0)
        k+=1
        ks.append(k)
        ys.append(c_w(x3))
    print("run time is:", time.time()-start)
    plt.plot(ks,ys)
    plt.show()
    return x3,k

# Run
# Aitken_l(0.00001,10*(-15),c_w_p)