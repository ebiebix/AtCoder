NUM = list(input().split(" "))
H = int(NUM[0])
N = int(NUM[1])
A = []
B = []
num = 0
for i in range(N):
    tmp = list(input().split(" "))
    A.append(int(tmp[0]))
    B.append(int(tmp[1]))
import numpy as np
A = np.array(A)
B = np.array(B)

while(H > 0):
    C = A/B
    index = np.argmax(C)
    if (int(A[index])<=H):
        H -= int(A[index])
        num += int(B[index])
    else:
        for i in range(A.size):
            A[i]=H
print(num)