for _ in range(int(input())):
    N, K = map(int,input().split())
    S = input()
    values = list(S)
    count = 0 
    flag = 0
    for i in range(len(values)):
        if values[i] == '*':
            count += 1
        else:
            count=0
        if count >= K:
            flag = 1
            break
    if flag:
        print('YES')
    else:
        print('NO')