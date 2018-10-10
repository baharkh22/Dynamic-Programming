# Uses python3
import sys

def get_change(m):
    #write your code here
    arr = [1,3,4]
    table = [0] * (m+4) 
    table[1]=1
    table[3]=1
    table[4]=1
    for i in range(1,m+1):
        
        if table[i]!=0:
            continue
        tmp=[]
        for j in range(0,len(arr)): 
            if (i-arr[j])<0:
                continue
            else:
                tmp.append(table[i-arr[j]]+1)
        tmp2=min(tmp)
        table[i]=tmp2
                 
    return table[m]        

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
