from queue import Queue
r, c = map(int, input().split(' '))
sy, sx = map(int, input().split(' '))
gy, gx = map(int, input().split(' '))
C = [[s for s in input()] for _ in range(r)]
print(C)

###関数DFS
dx = [0,0,1,-1]
dy = [-1,1,0,0]

q= Queue()
ans = 0
def BFS(graph,start_point = [sy,sx],goal_point = [gy,gx]):
    global ans
    not_visited = []
    not_visited=[[True for i in range(c)] for j in range(r)]
    q.put([start_point])#1.始点のノードを探索待ちスタックに追加
    not_visited[start_point[0]][start_point[1]] = False
    while not q.empty():#2.探索待ちスタックにノードが無ければ終了
        now_point = q.get()#2.探索待ちスタックにノードがあれば取り出す
        #print(now_point)
        valid_pos = []
        for n in now_point:
            print(n)
            for i in range(4):
                if n == goal_point:#3.取り出したノードが目的のノードであれば探索終了
                        ans += 1
                        print(ans,'uuuuu')
                        return False
                else:
                    print(n)
                    #print(n[0],dy[i],n[1],dx[i])
                    serch_point = [n[0]+dy[i],n[1]+dx[i]]#4.取り出したノードに隣接するノード
                    if 0 <= serch_point[0] < r and 0 <= serch_point[1] < c:#4.隣接するノードが迷路の範囲内かどうか判定
                        if graph[serch_point[0]][serch_point[1]] != "#" and not_visited[serch_point[0]][serch_point[1]]:#4.未探索のノードを探索待ちスタックに追加
                            #q.put([[serch_point[0],serch_point[1]]])
                            not_visited[serch_point[0]][serch_point[1]] = False
                            valid_pos.append([[serch_point[0], serch_point[1]]))
            if (len(valid_pos) != 0):
                q.put(valid_pos)
            ans += 1
    return True
if BFS(C, [sy-1,sx-1], [gy-1,gx-1]):
    print(ans-1)

#############3

# while not q.empty():
#     pos = q.get()
#     print(pos)
#     valid_pos = []
#     for p in pos:
#         for m in move:
#             y, x = p[0]+m[0], p[1]+m[1]
#             if y == gy and x == gx:
#                 ans += 1
#                 print(ans)
#                 exit()
#             else:
#                 C[y-1][x-1] == '.':
#                 C[y-1][x-1] = '#'
#                 valid_pos.append((y, x))
#     if len(valid_pos) != 0:
#         q.put(valid_pos)
#     ans += 1
# print(ans-1)