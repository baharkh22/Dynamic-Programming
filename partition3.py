# Uses python3
import sys
import itertools

def issum(Sum_,A):
    table={}
    for i in range(0,len(A)+1):
       for j1 in range(0,Sum_+1):
           for j2 in  range(0,Sum_+1):
                   table[i,j1,j2]=0
    table[0,0,0]=1
    A.insert(0,0)
    for i in range(1,len(A)):
        for j1 in range(0,Sum_+1):            
            for j2 in range(0,Sum_+1):
                    table[i,j1,j2]=0
                    tmp1 = 0 if j1<A[i] else table[i-1,j1-A[i],j2]
                    tmp2 = 0 if j2<A[i] else table[i-1,j1,j2-A[i]]
                    table[i,j1,j2,j3] = tmp1 | tmp2                       
    return table[i,Sum_,Sum_,Sum_]

def partition3(A):
    sum_=sum(A)
    if sum_%3 != 0:        
        return 0
    else:
        sum2=int(sum_/3)    
        return issum(sum2,A)             
            
        

if __name__ == '__main__':
   n=int(input())
   S=list(map(int,input().split()))
   if n<3:
       print('0')
   else:
       print(partition3(S))

