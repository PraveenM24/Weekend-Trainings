N = int(input())
budget = list()
revenue = list()
for _ in range(N):
    budget.append(int(input()))
budget.sort()
for index in range(len(budget)):
    max_revenue = budget[index] * (N - index)
    revenue.append(max_revenue)
print(max(revenue))