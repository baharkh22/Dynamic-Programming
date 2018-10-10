# Uses python3
import sys

def optimal_weight(W, Ws):
    # write your code here
    table={}
    Ws.sort(reverse=True)

    Ws.insert(0,0)  

    for i in range(0,W+1):
        table[i,0]=0
    for j in range(0,len(Ws)):
        table[0,j]=0
 
    
    
    for j in range(1,W+1):
        for k in range(1,len(Ws)):
                if Ws[k]==j:
                    table[j,k]=Ws[k]
                    continue
                if Ws[k]>j:                        
                    table[j,k]=table[j,k-1]
                    continue
                tmp=[0]
                if Ws[k]<j:
                    tmp.append(table[j-Ws[k],k-1]+Ws[k])                        
                tmp.append(table[j,k-1])
                tmp.append(table[j-1,k])
                table[j,k]=max(tmp)
                    
                    
                    

                    
    return table[j,k]

if __name__ == '__main__':
    W, n = list(map(int, input().split()))
    Ws = list(map(int, input().split()))
    print(optimal_weight(W, Ws[0:n]))
