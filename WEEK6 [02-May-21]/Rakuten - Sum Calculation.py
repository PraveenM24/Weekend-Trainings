for _ in range(int(input())):
    N = int(input())
    values = list(map(int, input().split()))
    index_sum = []
    for i in range(N):
        temp = 0
        for j  in range(N):
            temp += (values[j]//values[i])
        index_sum += [temp]
    print(sum(index_sum))
    
