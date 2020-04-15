n = int(input())
s = list(input())
rgb = s.count('R')*s.count('G')*s.count('B')
for r in (range(n-2)):
    for g in range(r+1,n-1):
        b = g-r+g
        if(b>=n):
            break
        if(s[r] != s[g] and s[r] != s[b] and s[g] != s[b]):
            rgb -= 1
print(rgb)