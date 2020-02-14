s = list(input())
n = len(s)
total = 0
for i in range(2 ** (n-1)):
    bag = []
    for j in range(n):
        if ((i >> j) & 1):
            bag.append(s[j])
            bag.append('+')
        else:
            bag.append(s[j])
        #print(bag)
    bag = ''.join(bag)
    #print(bag)
    for m in bag.split('+'):
        total += int(m)
print(total)