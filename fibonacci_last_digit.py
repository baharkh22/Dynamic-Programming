# Uses python3

def calc_fib(n):
    x=[0]*(n+1)
    if (n >= 1):
        x[1]=1
        
    if (n>=2):
        x[2]=1
        
    if (n>=3):
        for i in range(n-1):
            x[i+2]=x[i+1]+x[i]
            x[i+2]=x[i+2] % 10
            
    return x[n] % 10

if __name__=='__main__':    
    n = int(input())
    print(calc_fib(n))

