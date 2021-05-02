def find_gcd(x, y):
    while(y):
        x, y = y, x%y
    return x
N = int(input())
A = list(map(int, input().split()))
num1 = A[0]
num2 = A[1]
gcd = find_gcd(num1, num2)
for i in range(2, len(A)):
    gcd = find_gcd(gcd, A[i])
print(gcd)
