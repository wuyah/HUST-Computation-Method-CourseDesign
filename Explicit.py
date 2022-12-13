import math

def expilict_3(eps, D, Re=5813924.33689002):
    # eps: \epsilon, D: D, Re: Re
    # 以下是计算过程
    a = 2/math.log(10)
    b = eps/(3.7*D)
    d =( math.log(10)/5.02)*Re
    s = b*d+math.log(d)
    q = s**(s/(s+1))
    g = (b*d+math.log(d/q))
    z = math.log(q/g)
    delta = (g/(g+1))*z
    delta_CFA = delta*(1+(z/2)/((g+1)**2+(z/3)*(2*g-1)))
    tmp = a*(math.log(d/q)+delta_CFA)
    return (1/tmp)**2

expilict_3(0.00002,0.6)