import sys
sys.setrecursionlimit(10**6) # 재귀함수의 한계 설정
input = sys.stdin.readline

# 5. DFS 함수
def dfs(idx):
    global visited,graph,answer,order
    visited[idx] = True
    answer[idx] = order
    order+=1
    
    for i in graph[idx]:
        if not visited[i]:
            dfs(i)

# 0. 입력 및 초기화
N,M,R = map(int,input().split()) # 띄어쓰기를 기준으로 분리하여 매핑
MAX = 100000 + 10
graph = [[]for _ in range(N+1)]
visited = [False]* MAX
answer = [0] * MAX
order = 1

# 1. graph에 연결정보 채우기
for _ in range(M):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
    
# 2. 내림차순 정렬
for i in range(1, N+1):
    graph[i] = sorted(graph[i],reverse=True)

# 3. DFS 호출
dfs(R)

# 4. 출력
for i in range(1, N+1):
    print(answer[i])