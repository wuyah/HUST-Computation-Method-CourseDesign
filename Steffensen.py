import time
from matplotlib import pyplot as plt
from Bi import c_w
#x0: 起始位置; tol: 精确值; func: 需要求解的函数
def Steffsen(x0,tol,func):
    plt.xlabel("k")
    plt.ylabel("f(x)")
    plt.title("Fig4: Steffsen Method k-f(x) image")
    start = time.time()
    y0 = func(x0)
    x1 = x0 - y0**2/(y0-func(x0-y0))
    ys = [y0,func(x1)]
    k=1
    ks = [0,k]
    while abs(x1-x0)>tol:
        x0 = x1
        y0 = func(x0)

        # 避免除0错误
        if func(x0) == 0:
            end = time.time()
            plt.plot(ks,ys)
            plt.show()
            print("run time is:", end - start)
            return k, x0
        
        x1 = x0 - y0**2/(func(x0)-func(x0-y0))
        k += 1
        ks.append(k)
        ys.append(func(x1))
        
    print("run time is:", time.time() - start)

    plt.plot(ks,ys)
    
    plt.show()
    return x1

# Run
# Steffsen(0.0104815, 10*(-15), c_w)