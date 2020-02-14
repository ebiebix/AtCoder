n = int(input())
T = []
for i in range(n):
    t = int(input())
    T.append(t)
total = 101
for i in range(2**n):
    bag_a = []
    bag_b = []
    for j in range(n):
        if ((i>>j)&1):
            bag_a.append(T[j])
        else:
            bag_b.append(T[j])
    if(max([sum(bag_a),sum(bag_b)])<total):
        total = max([sum(bag_a),sum(bag_b)])
print(total)