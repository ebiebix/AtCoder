n  = int(input())
A = list(map(int,input().split()))
l = []
from collections import Counter
counter = Counter(A)
total = 0
def choose2(n):
    return n*(n-1)/2
for i in counter.most_common():
    c = choose2(i[1])
    total += c

for i in A:
    print(int(total-choose2(counter[i])+choose2(counter[i]-1)))