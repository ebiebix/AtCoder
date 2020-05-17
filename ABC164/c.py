n = int(input())
G = []
for i in range(n):
    g = input()
    G.append(g)
G = set(G)
print(len(G))