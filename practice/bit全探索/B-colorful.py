n,k = map(int,input().split())
A = list(map(int,input().split()))
result = 1000000001*15
def j_cost(cost):
    c = 1
    for i in range(1,len(A)):
        if(max(cost[:i]) < cost[i]):
            c += 1
    #print(c,cost)
    if c >= k:
        return True
    else:
        return False

for i in range(2**n):
    cost = [0]*len(A)
    for j in range(1,n):
        if((i>>j)&1):
            total = [x + y for (x,y) in zip(A[:j],cost[:j])]
            if(max(total)>=A[j]):
                cost[j] = max(total)+1-A[j]
            else:
                cost[j] = 0
    #print(cost,[x + y for (x,y) in zip(A,cost)])
    if(sum(cost) < result and j_cost([x + y for (x,y) in zip(A,cost)])):
        result = sum(cost)
print(result)
