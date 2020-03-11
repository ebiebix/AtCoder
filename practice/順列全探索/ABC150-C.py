import itertools
n = int(input())
A  = tuple(map(int,input().split()))
B  = tuple(map(int,input().split()))
Z = list(itertools.permutations(range(1,n+1)))
a = 0
b = 0
for i,z in enumerate(Z):
  #print(z,A)
  if(z == A):
    a = i+1
  if(z == B):
    b = i+1
print(abs(a-b))