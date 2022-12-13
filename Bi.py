import time
import math
from matplotlib import pyplot as plt

def c_w(f,eps=0.00002,d=0.6,re=5813924.33689002):
    tmp = 2*math.log10( eps/(3.7*d)+2.51/( re*math.sqrt(f)) )
    return (1/(math.sqrt(f)))+ tmp

# ------二分法------

# 假定左侧一定为负数
# left 是左侧边界，right是右侧边界
def bi(left, right, e,func):
    start = time.time()
    mid = (left+right)/2
    k = 0
    m = 1+(math.log(right-left)-math.log(2*e))//math.log(2)
    dotPath = [mid]
    times = [0]
    while k<=m:
        # 中间值大于0, 则根应当在左侧，需要更新右侧区间
        if func(mid) == 0:
            mid = mid
            return k, mid
        elif func(left)*func(mid) < 0:
            right = (left+right)/2
        else:
            left = (left+right)/2
        mid = (left+right)/2
        dotPath.append(mid)
        k+= 1
        times.append(k)
    y = [func(i) for i in dotPath]
    print("Run time is:", time.time()-start)

    plt.plot(times, y)
    plt.plot(times, [0]*len(dotPath))
    plt.show()
    return mid,k

# bi(0.00001,0.02, 10**(-15), c_w)