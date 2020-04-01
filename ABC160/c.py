k,n = map(int,input().split())
A = list(map(int,input().split()))
result = 1000001
S = [0]
s = 0

for n,i in enumerate(A):
    if(n <= len(A)-2):
        s = A[n+1] - A[n]
        S.append(s)
S.append(k-A[len(A)-1]+A[0])
#print(S)
tmp = 0
for s in range(len(S)):
    tmp += S[s]
    S[s] = tmp
#print(S)


for i in range(len(S)):
    if(i == 0):
        ans = S[len(S)-2] - S[0]
        if(result>ans):
            #print(result,'1')
            result = ans
    else:
        ans = S[len(S)-1]- S[i] + S[i-1] - S[0]
        if(result>ans):
            #print(result,'2')
            result = ans
A.reverse()
S = [0]
for n,i in enumerate(A):
    if(n <= len(A)-2):
        s = k - A[n]
        S.append(s)
S.append(k)
#print(S)

for i in A:
    s += i
    S.append(s)
for i in range(len(S)):
    if(i == 0):
        S[len(S)-2] - S[0]
        if(result>ans):
            #print(result,'3')
            result = ans
    else:
        ans = S[len(S)-1]- S[i] + S[i-1] - S[0]
        if(result>ans):
            #print(result,'4')
            result = ans
print(result)