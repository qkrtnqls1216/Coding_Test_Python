# 키워드: 네트워크 상에서 연결되어 있다.

def dfs(idx):
    global visited, graph, answer # 3개를 참조하겠다.
    visited[idx] = True
    answer +=1
    
    # 방문하지 않은 경우
    for i in range(1,  N+1):
        if not visited[i] and graph[idx][i]:
            dfs(i) # 재귀함수

# 입력 및 초기화
N = int(input())
M = int(input())

# 2차원 불리언 배열을 false로 초기화
graph = [[False] * (N+1) for _ in range(N+1)] # 하나의 행이 N+1번 반복되어 행도 N+1 열도 N+1이 된다.
visited = [False] * (N+1)
answer = 0

# graph에 연결 정보 채우기
for _ in range(M):
    x,y = map(int, input().split())
    # input을 받고 그대로가 아닌 띄어쓰기를 기준으로 나눠서 사용
    # 그것을 int형태로 mapping(변환)해서 사용할 것
    graph[x][y] = True
    graph[y][x] = True
    

# dfs(재귀함수) 호출
dfs(1) # 1부터 시작

# 출력
print(answer - 1)# 1번노드를뺀 것 출력