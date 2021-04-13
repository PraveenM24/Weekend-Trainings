values = list(map(int,input().split()))
final = set(values)

if len(final) != len(values):
    print('YES')
else:
    print('NO')