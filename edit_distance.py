# Uses python3
def edit_distance(X, Y):
    #write your code here
    
    XL=len(X)
    YL=len(Y)
    
    Dis={}
    for i in range(0,XL+1):
        Dis[i,0]=i
        
    for j in range(0,YL+1):
        Dis[0,j]=j
    
    for i in range(1,XL+1):
        for j in range(1,YL+1):
            if X[i-1]==Y[j-1]:
                Dis[i,j]=Dis[i-1,j-1]
            else:
                Dis[i,j]=min([Dis[i-1,j],Dis[i-1,j-1],Dis[i,j-1]])+1
    return Dis[XL,YL]

if __name__ == "__main__":
    X=input()
    Y=input()
    print(edit_distance(X,Y))
