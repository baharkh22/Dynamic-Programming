# Uses python3
import sys
import numpy as np      

def get_optimal_value(c, w, val):
    
    # write your code here
    WW=np.array(w)
    Val=np.array(val)
    V=Val/WW
    c2=0
    value=0
    while (c2<c and V.size!=0):
        a=V.argmax()
        V=np.delete(V,a)
        free=c-c2
        getW=free/WW[a]
        if getW>1:
            getW=1
        c2=c2+(WW[a]*getW)
        value= getW*Val[a] + value
        Val=np.delete(Val,a)
        WW=np.delete(WW,a)
    
    return value


if __name__ == "__main__":
    data = list(map(int, input().split()))
    n, capacity = data[0:2]
    values = []
    weights = []
    for i in range(0,n):
        tmp1,tmp2 =map(int,input().split())
        values.append(tmp1)
        weights.append(tmp2)
        
    x=get_optimal_value(capacity, weights, values)
    print(str(x))
