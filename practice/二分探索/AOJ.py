http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_B&lang=ja
n = int(input())
S = list(map(int,input().split()))
q = int(input())
T = list(map(int,input().split()))
total = 0
def bi_serch(S:list, i:int):
    low = 0
    high = len(S)-1
    while low <= high:
        mid = (low + high)//2
        guess = S[mid]
        if guess == i:
            return True
        elif guess > i:
            high = mid - 1
        else:
            low = mid + 1
    return False

for i in T:
    if(bi_serch(S,int(i))):
        total += 1
print(total)