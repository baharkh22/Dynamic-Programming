# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    S=list(segments)
    flag=0
    S2=[]
    #write your code here
    while len(S)>1:
        tmp=S[0]
        del S[0]
        Z=[]
        for x in S:
            z=x & tmp
            Z=Z+list(z)
        Z2=set(Z)
        Max_coverage=[]
        Num=0
        for i in Z2:
            tmp=Z.count(i)
            if tmp>Num:
                Num=tmp
                Max_coverage=i
                
        ind_del=[]
        if Num>0:
            count=0
            for i in S:
                
                if Max_coverage in i:
                     ind_del.append(count)
                count = count+1 
        ind_del=sorted(ind_del,reverse=True)
        
        for i in ind_del: del S[i]
        if (type(Max_coverage) is list) and len(Max_coverage)==0:
            ttmp=list(tmp)
            S2.append(ttmp[0])
        else:
            S2.append(Max_coverage)
                
            
    if len(S)==1:
        tmp=list(S[0])
        S2.append(tmp[0])        

    
    return list(set(S2))


if __name__ == '__main__':
    N=int(input())
    Y=()
    for i in range(0,N):
        X=list(map(int,input().split()))
        X2=set(range(X[0],X[1]+1))
        Y=Y+(X2,)
    Z=optimal_points(Y)
    print(len(Z))
    for i in Z:
        print(i,end=' ')
    print('')
    #n, *data = map(int, input.split())
    #print('hi')
    #segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    #Fpoints = optimal_points(segments)
    #print(len(points))
    #for p in points:
     #   print(p, end=' ')
