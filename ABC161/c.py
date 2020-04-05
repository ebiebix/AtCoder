n,k = map(int,input().split())
j = n%k
if(j>abs(j-k)):
    print(abs(j-k))
else:
    print(j)