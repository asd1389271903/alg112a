#由chatgpt輔助
import numpy as np

def solve_polynomial(coefficients):
    roots = np.roots(coefficients)
    real_roots = [root.real for root in roots if np.iscomplex(root) == False] 
    return real_roots

#x^8+3x^2+1=0->[1,0,0,0,0,0,3,0,1] x^5+1=0->[1,0,0,0,0,1]
coefficients = [1,-4,4]
roots = solve_polynomial(coefficients)
if(len(roots)==0):
    print("沒找到")
else:
    print("根：", roots)
