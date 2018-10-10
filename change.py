# Uses python3
import sys

def get_change(m):
    #write your code here
    a=m%10
    num10=int((m-a)/10)
    b=a%5
    num5=int((a-b)/5)
    
    x=num10 + num5 + b
    
    
    return x

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
