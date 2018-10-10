# Uses python3
import sys

def get_change(m):
    #write your code here
    arr = [1,3,4]
    table = [0] * (m+4) 
    table[1]=0
    table[2]=1
    table[3]=1
    tmp=[0] * (m+4)
    tmp[1]=1
    tmp[2]=2
    tmp[3]=3
    for i in range(2,m+1):

        if table[i]!=0:
            continue
        tmptmp=[]
        tmptmp2=[]
        if i%3 == 0:

            tmptmp.append(3)
            tmptmp2.append(table[int(i/3)])
        if i%2 == 0:

            tmptmp.append(2)
            tmptmp2.append(table[int(i/2)])
            


        tmptmp.append(1)
        tmptmp2.append(table[i-1])            
        ind=tmptmp2.index(min(tmptmp2))
        table[i]=min(tmptmp2)+1
        tmp[i]=tmptmp[ind]

    print(table[m])
    tmp2=m
    vals=[m]
    while tmp2>1:
        if tmp[tmp2]==1:
            tmp2=tmp2-1
            vals.insert(0,tmp2)
        elif tmp[tmp2]==2:
            tmp2=int(tmp2/2)
            vals.insert(0,tmp2)
        elif tmp[tmp2]==3:
            tmp2=int(tmp2/3) 
            vals.insert(0,tmp2)
                        
    print(' '.join(str(x) for x in vals))        
    
if __name__ == '__main__':
    m = int(input())
    get_change(m)

