# 方法 1
def power2n(n):
    return 2**n

# 方法 2a：用遞迴
def power2na(n):
    if n==0:
        return 1;
    elif n>=1:
        return power2na(n-1)+power2na(n-1)
    # power2n(n-1)+power2n(n-1)

# 方法2b：用遞迴
def power2nb(n):
    if n==0:
        return 1;
    elif n>=1:
        return 2*power2na(n-1)
    # 2*power2n(n-1)

# 方法 3：用遞迴+查表
def power2nc(n):
    power=[None]*100
    if n==0:
        return 1
    elif n==1:
        return 2
    elif power[n] is not None:
        return power[n]
    else:
        power[n]=power2nc(n-1)+power2nc(n-1)
        return power[n]
    # if ....
    # power2n(n-1)+power2n(n-1)

n=int(input("次方大小:"))
print("方法1:",power2n(n))
print("方法2:",power2na(n))
print("方法3:",power2nb(n))
print("方法4:",power2nc(n))
