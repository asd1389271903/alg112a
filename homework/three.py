def truthtable(n):
    arr=[]
    return next(n,arr)

def next(n,arr):
    l=len(arr)
    if l==n:
        print(arr)
        return
    for x in range(n):
        if not x in arr:
            arr.append(x)
            next(n,arr)
            arr.pop()

n=int(input("輸入陣列大小:"))
truthtable(n)

#參考老師的permutation 已理解