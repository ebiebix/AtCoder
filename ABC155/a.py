a,b,c = map(int,input().split())
if (a == b and a==c and b == c):
    print('No')
elif (a == b or b == c or c == a):
    print('Yes')
else:
    print('No')