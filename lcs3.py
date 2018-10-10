#Uses python3

import sys

def lcs2(a, b,c):
    #write your code here
    lc={}
    for i in range(0,len(a)+1):
        for k in range(0,len(c)+1):
            lc[i,0,k]=0
        for j in range(0,len(b)+1):
            lc[i,j,0]=0
            
    for j in range(0,len(b)+1):
        for k in range(0,len(c)+1):
            lc[0,j,k]=0  
        for i in range(0,len(a)+1):
            lc[i,j,0]=0      
    
    
    
    for i in range(1,len(a)+1):
        for j in range(1,len(b)+1):
            for k in range(1,len(c)+1):

                if a[i-1]==b[j-1] and a[i-1]==c[k-1]:
                    lc[i,j,k]=lc[i-1,j-1,k-1]+1
                else:
                    tmp1=lc[i-1,j,k]
                    tmp2=lc[i-1,j-1,k]
                    tmp3=lc[i,j-1,k]
                    tmp4=lc[i-1,j,k-1]
                    tmp5=lc[i-1,j-1,k-1]
                    tmp6=lc[i,j-1,k-1]
                    tmp7=lc[i,j,k-1]

                    tmp=max([tmp1,tmp2,tmp3,tmp4,tmp5,tmp6,tmp7])
                    lc[i,j,k]=tmp
                #if tmp==tmp1:
               #     lc[i,j]=lc[i-1,j]
              #  elif tmp==tmp2:
                 #   lc[i,j]=lc[i-1,j-1]
               # else:
                  #  lc[i,j]=lc[i,j-1]
    
    return lc[len(a),len(b),len(c)]

if __name__ == '__main__':
    n = int(input())
    data = list(map(int, input().split()))
    m = int(input())
    data2 = list(map(int, input().split()))
    m2 = int(input())
    data22 = list(map(int, input().split()))    
    
    data = data[:n]
    data2=data2[:m]
    data22=data22[:m2]

    print(lcs2(data, data2,data22))
