import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 5. dfs함수
def dfs(idx):
    global visited,graph,answer,order
    visited[idx] = True # index번째 노드를 방문했다는 걸 표기
    answer[idx] = order # 현재 idx에 order번째로 들어왔다고 담아주기
    order +=1 # order 증가
    
    for i in graph[idx]:
        if not visited[i]:
            dfs(i)

# 0. 입력 및 초기화 
N,M,R = map(int,input().split()) # 입력 값을 띄어쓰기를 기준으로 분리해서 int형으로 mappling
MAX = 100000 + 10 # 최대 10만개에서 여분 10개정도를 해준 것
graph = [[] for _ in range(N+1)] # 입력한 N개의 정점 만큼 빈리스트로 초기화
visited = [False] * MAX # 재방문방지를 위한 MAX만큼의 1차원배열 False로 초기화 
answer = [0]  * MAX
order = 1

# 1. gragh에 연결 정보 채우기
# M개의 간선정보를 받음
for _ in range(M):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
    
# 2. 오름차순 정렬
for i in range(1, N+1):
    graph[i]  = sorted(graph[i])

# 3. DFS 호출
dfs(R)

# 4. 출력
for i in range(1, N+1):
    print(answer[i])