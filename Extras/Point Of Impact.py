for _ in range(int(input())):
    N,K,x,y=map(int,input().split())
    if (x,y)==(N,N) or (x,y)==(N,0) or (x,y)==(0,N) :
        print(x,y)
    elif x==y:
        print(N,N)
    else:
        if x>y:
            va=N-x
            FCx,FCy=x+va,y+va
            SCx,SCy=y+va,x+va
            TCx,TCy=y-y,x-y
            FoCx,FoCy=x-y,y-y
        else:
            va=N-y
            FCx,FCy=x+va,y+va
            SCx,SCy=y+va,x+va
            TCx,TCy=y-x,x-x
            FoCx,FoCy=x-x,y-x
        K%=4
        if K==1:
            print(FCx,FCy)
        elif K==2:
            print(SCx,SCy)
        elif K==3:
            print(TCx,TCy)
        else:
            print(FoCx,FoCy)