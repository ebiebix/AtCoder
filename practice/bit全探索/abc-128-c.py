n,m = map(int,input().split())
for i range(2**n):
    for j in range(n):
        if((i>>j)&1):
            for p in range(m)