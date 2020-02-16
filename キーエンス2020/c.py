n,k,s = map(int,input().split())
L = []
if (s == 10**9):
    for i in range(k):
        L.append(10**9)
    for i in range(n-k):
        L.append(1)
else:
    for i in range(k):
        L.append(s)
    for i in range(n-k):
        L.append(s+1)
print(' '.join(map(str,L)))
