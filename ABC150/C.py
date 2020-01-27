n = int(input())
p = input().split(" ")
val_p = 0
for i in range(n):
    val_p+= 10**int((n-1)-i)*int(p[i])

q = list(input())
