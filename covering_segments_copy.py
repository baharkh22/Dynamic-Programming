# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    Opt=[]
    pointer=0
    S=list(segments)
    b = [el[1] for el in S]
    c=sorted(b,key=int)
    for j in c:
        b = [el[1] for el in S]
        ind=b.index(j)
        start=S[ind][0]
        
        if pointer<start:
            pointer=j
            Opt.append(j)
            del S[ind]
        else:
            del S[ind]   
            
    return Opt
    
            


if __name__ == '__main__':
    N=int(input())
    Y=()
    for i in range(0,N):
        X=list(map(int,input().split()))
        Y=Y+(X,)
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
