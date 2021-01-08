for _ in range(int(input())):
    N,K,D=map(int,input().split())
    A=sum(list(map(int,input().split())))
    if A<K:
        print(0)
    else:
        Quotient=A//K
        if Quotient<=D:
            print(Quotient)
        else:
            print(D)
        