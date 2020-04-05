import math
n,m = map(int,input().split())
X = []
Y = []
relationship = [[True if i == j else False for i in range(n)] for j in range(n)]
#print(relationship)
for i in range(m):
    x,y = map(int,input().split())
    X.append(x)
    Y.append(y)
X = list(map(lambda x:x-1,X))
Y = list(map(lambda x:x-1,Y))

for i in range(len(X)):
    relationship[X[i]][Y[i]] = True
    relationship[Y[i]][X[i]] = True

result = 0
for i in range(1,2**n):
    Index = []
    for j in range(n):
        if((i>>j)&1):
            Index.append(j)
    #print(Index)
    tmp = 0
    for j in Index:
        for k in Index:
            if(relationship[j][k] is True):
                tmp += 1
    if(tmp == len(Index)**2):
        #print(tmp)
        if(result<math.sqrt(tmp)):
            result = int(math.sqrt(tmp))
print(result)