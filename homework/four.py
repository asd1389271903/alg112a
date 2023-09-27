from numpy import arange
import math

f1=lambda x:((x**2)+1)/3 #x^2-3x=-1    x=(1+x^2)/3 自己的方法1(收斂)
f2=lambda x:(3/(x-4))+1  #(x-4) (x-1)=3  x=(3/(x-4))+1  2 發散
f3=lambda x:(1+x**2)/3 #同除x  f3=lambda x:3-(1/x)  3 發散

x1=x2=x3=1


def f(x) :
    # return x*x-4*x+1
    return math.pow(x,2)-(3*x)+1

for x in arange(-100, 100, 0.001):
    if abs(f(x)) < 0.001:
        print("x=", x, " f(x)=", f(x))


for i in range(20):
    x1, x2, x3 = f1(x1), f2(x2), f3(x3)
    print('x1:', x1, 'x2', x2, 'x3', x3)