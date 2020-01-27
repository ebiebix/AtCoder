B = list(input().split(" "))
h = int(B[0])
n = int(B[1])
A = list(input().split(" "))
sum = 0
for i in range(len(A)):
    sum += int(A[i])
if (h<=sum):
    print("Yes")
else:
    print("No")