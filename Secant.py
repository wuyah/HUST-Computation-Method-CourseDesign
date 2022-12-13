from matplotlib import pyplot as plt
import time
from Bi import c_w

# x0: 左边界; x1: 右边界; tol: 误差终止项; func: 需要求解0点的函数

def secant(x0,x1, tol,func):
    start = time.time()

    x2 = x1 - (x1-x0)*func(x1)/(func(x1)-func(x0))
    ys = [func(x2)]
    k = 1
    ks = [k]
    while abs(x2-x1)>=tol:
        x0 = x1
        x1 = x2
        x2 = x1 - (x1-x0)*func(x1)/(func(x1)-func(x0))
        k+=1
        ks.append(k)
        ys.append(func(x2))    
    # 计算运行时间
    print("Run time is:", time.time()-start)
    # 绘制结果表格
    plt.plot(ks,ys)
    plt.show()
    return x2,k

# Run
# secant(0.0001,0.02,10**(-323),c_w)