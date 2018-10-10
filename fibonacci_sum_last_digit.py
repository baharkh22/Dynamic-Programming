# Uses python3
import sys


def calc_fib(n):
    x=[0]*(n+1)
    if (n >= 1):
        x[1]=1
        
    if (n>=2):
        x[2]=1
        
    if (n>=3):
        for i in range(n-1):
            x[i+2]=x[i+1]+x[i]
            
    return x[n]



def calc_fib(n):
    x=[0]*1000000
    if (n >= 1):
        x[1]=1
        
    if (n>=2):
        x[2]=1
        
    if (n>=3):
        for i in range(n-1):
          #  print (x[i])
           # rint ('inside')
            if i>3 and x[i]==0 and x[i+1]==1:
                tmp=sum(x[1:i-1])
                tmp2=tmp*int(n/i)
                n=n%i
                tmp3=calc_fib(n)   
                x=[0]*2
                x[0]=tmp3
                x[1]=tmp2             
                break
            
            x[i+2]=x[i+1]+x[i]
            x[i+2]=x[i+2] % 10
        
    return sum(x[0:-1]) % 10

if __name__=='__main__':    
    n = int(input())
    print(calc_fib(n))


