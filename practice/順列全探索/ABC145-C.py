import itertools
import math
n = int(input())
l = list(itertools.permutations(range(n)))
X = []
Y = []
for i in range(n):
  x,y = map(int,input().split())
  X.append(x)
  Y.append(y)
result = []
for i in l:
  #print(i)
  d = 0
  for j in range(int(len(i))-1):
    d += math.sqrt((X[i[j]]-X[i[j+1]])**2 + (Y[i[j]]-Y[i[j+1]])**2)
    #print(d)
  result.append(d)
print(sum(result)/len(result))


