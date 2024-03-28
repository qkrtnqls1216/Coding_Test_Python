import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 4. DFS 함수 입력
def dfs(idx, count):
    global graph,visited,end,answer
    visited[idx] = True
    # index와 end가 동일한 경우
    if idx == end:
        answer = count # answer에 count 저장하고 return
        return
    
    # 그 다음 방문할 노드 탐색
    for i in range(1,N+1):
        if not visited[i] and graph[idx][i]:
            dfs(i, count + 1) # 촌수 count
    
    
# 0. 입력 및 초기화
N = int(input())
start,end = map(int,input().split())
M = int(input())
MAX = 100+10
graph = [[False] * MAX for _ in range(MAX)]
visited = [False] * MAX
answer = -1

# 1. graph에 연결정보 채우기
for _ in range(M):
    x,y = map(int,input().split())
    graph[x][y] = True
    graph[y][x] = True

# 2. DFS 호출
dfs(start,0) # 시작은 0촌 부터이므로 두번째인자 count를 0으로 초기화

# 3. 출력 
print(answer)