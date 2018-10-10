#Uses python3
import sys
import math
import statistics as stat

def search(x,val,strt,endd):
    
    if strt>=endd-1:
        return endd-1
    if x[strt]>=val:
        return strt
    if x[endd-1]<=val:
        return endd-1
    n=int((strt+endd)/2)
    
    if x[n]>val and x[n-1]<=val:
        return n
    elif x[n]<=val:
        y=search(x,val,n,endd)
        return y
    else:
        y=search(x,val,strt,n)
        return y
    
    
def euc_dis(X,Y):
    tmp = ((X[1]-X[0])**2 + (Y[1]-Y[0])**2) ** 0.5
    return round(tmp,15) 

def minimum_distance(x, y,Min,strt,endd):
    #write your code here

    if endd<=(strt+1):
            return Min
    elif endd == strt+2:
            return euc_dis(x[strt:endd],y[strt:endd])
    if Min == 0:
            return Min    

        
        
  #  l=(x[strt]+x[endd-1])/2
    pointer=int((strt+endd)/2)#strt
    l=x[pointer]
 #   for i in range(strt,endd):
 #       if x[i]<l:
#            pointer=pointer+1
    M1=Min
    M2=Min
    if pointer!=strt and pointer!=endd-1:        
        M1=minimum_distance(x,y,Min,strt,pointer)
        M2=minimum_distance(x,y,Min,pointer,endd)
    
    Min = min([M1,M2,Min])
    
    MM=Min
    X=[]
    Y=[]
    
    
    val1=l-Min
    L1=search(x,val1,strt+1,pointer)
    val2=l+Min
    L2=search(x,val2,pointer,endd)
    
    for i in range(L1-1,pointer):
            for j in range(pointer,L2):
                    if abs(y[i]-y[j]) < Min:
                        tmp=euc_dis([x[i],x[j]],[y[i],y[j]])
                        MM=min([MM,tmp])
    
        
    Min=MM               
    
    return(Min)
    
if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    N = int(input())
    XY=[]
    X=[]
    Y=[]
    for i in range(0,N):
        data = list(map(int,input().split()))
        XY.append(data)
        X.append(data[0])
        Y.append(data[1])
    
    x1=stat.stdev(X)
    y1=stat.stdev(Y)
    if y1>x1:
        XY.sort(key=lambda x: x[1])
        X=[i[1] for i in XY]
        Y=[i[0] for i in XY]
    else:          
        XY.sort(key=lambda x: x[0])
        X=[i[0] for i in XY]
        Y=[i[1] for i in XY]
        
    Min=((X[1]-X[0])**2 + (Y[1]-Y[0])**2) ** 0.5
    Dist=minimum_distance(X,Y,Min,0,len(X))
    print(str(Dist))
