for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    MaxValue = 0
    A.sort()
    i = 0
    j = 1 
    k = len(A)-1
    MaxValue = max(MaxValue, abs(A[i]-A[j]) + abs(A[j]-A[k]) + abs(A[k]-A[i]))
    j = 0
    MaxValue = max(MaxValue, abs(A[i]-A[j]) + abs(A[j]-A[k]) + abs(A[k]-A[i]))
    i = 1
    j = 1
    MaxValue = max(MaxValue, abs(A[i]-A[j]) + abs(A[j]-A[k]) + abs(A[k]-A[i]))
    print(MaxValue)