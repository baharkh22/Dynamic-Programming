#Uses python3

import sys
import numpy as np

def max_dot_product(a, b):
    #write your code here
    
    Y=0
    
    while len(a) != 0:
        ind1=a.index(max(a))
        ind2=b.index(max(b))
    
        Y=Y+a[ind1]*b[ind2]
        del a[ind1]
        del b[ind2]
    
    
    return Y
    
if __name__ == '__main__':
    N=int(input())
    As = list(map(int,input().split()))
    Bs = list(map(int,input().split()))
    As=As[0:N]
    Bs=Bs[0:N]
    Y=max_dot_product(As,Bs)
    print(str(Y))
    
