k = int(input())
import itertools
def GCD(a,b):
    if(a%b == 0):
        return b
    else:
        return GCD(b,a%b)
total = 0
for a in range(1,k+1):
    for b in range(1,k+1):
        for c in range(1,k+1):
            total += GCD(GCD(a,b),c)
print(total)