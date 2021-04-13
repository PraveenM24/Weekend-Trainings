#Input
for _ in range(int(input())):
    #Process
    values = list(map(float,input().split()))
    result = 1
    for i in values:
        result *= i # result = result * i
    time = 100/result
    time = round(time, 2)
    if time < 9.58:
        print('YES')
    else: 
        print('NO')
    