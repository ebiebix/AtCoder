n = int(input())
XL = [list(map(int,input().split())) for i in range(n)]

XL.sort(key = lambda x:sum(x))
ans = 0
f = -1000000001
for x,l in XL:
    if x - l >= f:
        ans += 1
        #print(f)
        f = x + l
print(ans)