A = list(input().split(" "))
N = int(A[0])
K = int(A[1])
H = list(input().split(" "))
sum = 0
H.sort()
for i in range(K):
    H[N-1-i] = "0"
for i in range(N):
    sum += int(H[i])
print(sum)
