# Uses python3
def calc_fib(n,m):
    x=[0]*10000
    if (n >= 1):
        x[1]=1
        
    if (n>=2):
        x[2]=1
        
    if (n>=3):
        for i in range(n-1):
          #  print (x[i])
           # rint ('inside')
            if i>3 and x[i]==0 and x[i+1]==1:                
                n=n%i
                break
            x[i+2]=x[i+1]+x[i]
            x[i+2]=x[i+2] % m
        for j in range(i,n-1):   
             x[i+2]=x[i+1]+x[i]
             x[i+2]=x[i+2] % m
    return x[n] % m

if __name__=='__main__':    
    n = int(input())
    x=calc_fib(n,10)
    y=calc_fib(n+1,10)
    
    print((x*y)%10)

