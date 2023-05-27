#78페이지
import sys
sys.setrecursionlimit(10**6) #재귀호출 횟수가 1000회 제한되어 있는 것 늘려주기
input = sys.stdin.readline

#dfs탐색(탐색할 그래프, 시작 노드, 방문 여부 리스트)
def dfs(graph, node, visited) :
    visited[node] =True  #시작 노드 방문
    for i in graph[node] : #인접 노드 방문
        if not visited[i]: #방문하지 않았따면
            dfs(graph, i, visited) #해당 노드를 시작노드로!

#그래프 입력
N,M = map(int, input().split())
graph = [[i] for i in range(N+1)]
for i in range(M) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

#방문 여부 리스트
visited = [False]*(N+1)
#연결 요소 개수
cnt =0
for i in range(1,N+1) :
    if not visited[i] :
        cnt+=1
        dfs(graph,i,visited)

print(i)