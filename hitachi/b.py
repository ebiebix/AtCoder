a,b,m = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
#print(A,B)

X = []
Y = []
C = []
total = 2*10**5
for i in range(m):
    x,y,c = map(int,input().split())
    X.append(x)
    Y.append(y)
    C.append(c)
for i in range(m):
    result = int(A[int(X[int(i)])-1])+int(B[int(Y[int(i)])-1])-int(C[int(i)])
    if (total > result):
        total = result
#print(int(min(A))+int(min(B)))
if(int(min(A))+int(min(B))>total):
    print(total)
else:
    print(int(min(A))+int(min(B)))