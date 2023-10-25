import random

def hillClimbing(f, p, h=0.01):
    failCount = 0                    
    while (failCount < 10000):       
        fnow = f(p)                  
        p1, f1 = neighbor(f, p, h)
        if f1 >= fnow:        
            fnow = f1
            p=p1
            print('p=', p, 'f(p)=', fnow)
            failCount = 0            
        else:                        
            failCount = failCount + 1
    return p,fnow                

def neighbor(f,p,h):
    i=len(p)
    p1=p.copy()
    for z in range(i):
        p1[z] += random.uniform(-h, h)
    f1 =f(p1)
    return p1 , f1

def f(p):
    #return -1 * ( x*x -2*x + y*y +2*y - 8 )
    return -1*(p[0]**2+p[1]**2+p[2]**2)

=hillClimbing(f, [2,1,3])
