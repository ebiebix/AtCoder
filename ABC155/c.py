n = int(input())
S = []
for i in range(n):
    s = input()
    S.append(s)
S.sort()
A = list(set(S))
A.sort()
#print(A)
#print(S)
NUM =[0]*len(A)
j = 0
for i in range(len(S)):
    if(i+1<len(S)):
        if (S[i] == S[int(i)+1]):
            NUM[j] = NUM[j]+ 1
        else:
            j += 1
import numpy as np
b = np.argmax(NUM)
#print(NUM,b)
for e,i in enumerate(NUM):
    #print(NUM[b])
    if (i == NUM[b]):
        print(A[e])