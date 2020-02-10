s = list(input())
#print(s)

for i in range(len(s)):
    s[i]='x'
print(''.join(s))