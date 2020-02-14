s = list(map(int,input()))
n = len(s)
for i in range(2**(n-1)):
    bag = []
    for j in range(n-1):
        if ((i>>j)&1):
            bag.append(s[j])
            bag.append('+')
        else:
            bag.append(s[j])
            bag.append('-')
    bag.append(s[n-1])
    bag = list(map(str,bag))
    #ss = ''.join(bag)
    #print(bag)
    total = int(bag[0])
    for m,sss in enumerate(bag):
        if(sss == '+'):
            total += int(bag[m+1])
        elif(sss == '-'):
            total -= int(bag[m+1])
    if(total==7):
        print(''.join(bag)+'=7')
        exit()