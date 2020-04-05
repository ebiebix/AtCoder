n,m = map(int,input().split())
A = list(map(int,input().split()))

total = sum(A)
A.sort()
A.reverse()
com = 0
for i in A:
    if(i < total/(4*m)):
        break
    else:
        com += 1
if(com>=m):
    print('Yes')
else:
    print('No')