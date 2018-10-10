# Uses python3
import sys

def optimal_summands(n):
    summands=[]
    pointer=0
    while n>pointer:
        pointer = pointer + 1
        n=n-pointer
        if n> pointer:
            summands.append(pointer)
        else:
            summands.append(n+pointer)
    #write your code here
    return summands

if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
