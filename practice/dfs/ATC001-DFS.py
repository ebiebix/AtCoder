##https://kinaonao.blogspot.com/2018/04/blog-post.html

####データの読み込み
H,W = map(int,input().split())
graph = []
for i in range(H):
  s = list(input())
  if "s" in s:
    start_point = [i,s.index("s")]
  if "g" in s:
    goal_point = [i,s.index("g")]
  graph.append(s)
#print(start_point,goal_point,graph)

###関数DFS
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def DFS(graph,start_point,goal_point):
  not_visited = []
  not_visited=[[True for i in range(W)] for j in range(H)]
  stack = [start_point]#1.始点のノードを探索待ちスタックに追加
  #print(graph)
  not_visited[start_point[0]][start_point[1]] = False
  while len(stack) != 0:#2.探索待ちスタックにノードが無ければ終了
    now_point = stack.pop()#2.探索待ちスタックにノードがあれば取り出す
    for i in range(4):
      if now_point == goal_point:#3.取り出したノードが目的のノードであれば探索終了
        print("Yes")
        return False
      else:
        #print(now_point[0]+dx[i],now_point[1]+dy[i])
        serch_point = [now_point[0]+dx[i],now_point[1]+dy[i]]#4.取り出したノードに隣接するノード
        if 0 <= serch_point[0] < H and 0 <= serch_point[1] < W:#4.隣接するノードが迷路の範囲内かどうか判定
          if graph[serch_point[0]][serch_point[1]] != "#" and not_visited[serch_point[0]][serch_point[1]]:#4.未探索のノードを探索待ちスタックに追加
            stack.append([serch_point[0],serch_point[1]])
            not_visited[serch_point[0]][serch_point[1]] = False
  return True
if DFS(graph, start_point, goal_point):
  print("No")