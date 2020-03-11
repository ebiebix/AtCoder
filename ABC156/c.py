n = int(input())
N = list(map(int,input().split()))
result = 1000001
for i in range(100):
    total = 0
    for j in range(n):
        total += (i - N[j])**2
    if (result>total):
        result = total
print(result)
