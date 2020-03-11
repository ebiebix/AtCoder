n,a,b = map(int,input().split())
total = a+b
if (n%total<=a):
    result = int(n/total)*a+n%total
else:
    result = int(n/total)*a+a
print(result)