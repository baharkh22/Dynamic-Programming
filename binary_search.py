# Uses python3
import sys

def binary_search(a, x,beg,en):
    n=int((en-beg)/2)+beg


    
        
    if x==a[n]:
        return n
        
    if beg==en:
        return -1
        
    elif x>a[n]:
        m=binary_search(a,x,n+1,en)
        if m== -1:
            return -1
        else:
            return m
    else:
        m=binary_search(a,x,beg,n)
        if m== -1:
            return -1
        else:    
            return m        
    
    # write your code here

if __name__ == '__main__':
    data = list(map(int, input().split()))  
    n = data[0]
    a = data[1 : n + 1]
    data = list(map(int, input().split()))
    n2 = data[0]
    a2 = data[1 : n2 + 1]    
    for x in a2:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x,0,len(a)-1), end = ' ')
