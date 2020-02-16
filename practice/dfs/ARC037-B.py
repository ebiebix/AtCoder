import numpy as np
n, m = map(int, input().split())
g = [[] * n for i in range(n)]

#隣接行列もどきを取得
for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)
print(g)

not_visited = [True for i in range(n)]
ans = 0



#頂点をループ
for i in range(n):
    if not_visited[i]:
        flag = True