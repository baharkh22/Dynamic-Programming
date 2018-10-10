# Uses python3
import sys

def gcd(a, b):
    if a>b:
        x=a
        y=b
    else:
        x=b
        y=a
    
    
    while 1:
        tmp=x%y
        if tmp==0:
            return y
        else:
            x=y
            y=tmp
         
                


if __name__ == "__main__":
    tmp = input()
    a, b = map(int, tmp.split())
    x=gcd(a,b)
    tmp=int(b/x)
    y=int(a*tmp)
    print(y)

