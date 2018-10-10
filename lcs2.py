#Uses python3

import sys

def lcs2(a, b):
    #write your code here
    lc={}
    for i in range(0,len(a)+1):
        lc[i,0]=0
    for j in range(0,len(b)+1):
        lc[0,j]=0        
    
    
    
    for i in range(1,len(a)+1):
        for j in range(1,len(b)+1):
            if a[i-1]==b[j-1]:
                lc[i,j]=lc[i-1,j-1]+1
            else:
                tmp1=lc[i-1,j]
                tmp2=lc[i-1,j-1]
                tmp3=lc[i,j-1]
                tmp=max([tmp1,tmp2,tmp3])
                lc[i,j]=tmp
                #if tmp==tmp1:
               #     lc[i,j]=lc[i-1,j]
              #  elif tmp==tmp2:
                 #   lc[i,j]=lc[i-1,j-1]
               # else:
                  #  lc[i,j]=lc[i,j-1]
    
    return lc[len(a),len(b)]

if __name__ == '__main__':
    n = int(input())
    data = list(map(int, input().split()))
    m = int(input())
    data2 = list(map(int, input().split()))
    
    data = data[:n]
    data2=data2[:m]

    print(lcs2(data, data2))
