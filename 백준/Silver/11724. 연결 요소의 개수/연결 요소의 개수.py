import sys
sys.setrecursionlimit(10**6) # 재귀함수로 호출 할 수 있는 횟수를 10의 6제곱(100만번)으로 제한
input = sys.stdin.readline # 코데 문제 풀때 입출력을 빠르게 하기 위해 사용하는 부분
# 시스템에 있는 input 값을 빠르게 읽어서 성능을 높일 수 있음
#### 위 3줄은 항상 넣어주는 것이 좋다.

    # 4. DFS함수 호출
def dfs(idx):
    global visited,graph # 참조하겠다.
    visited[idx] = True
    
    for i in range(1,N+1):
        # 방문한 적이 없다면 나랑 연결되어있는게 맞는지 확인
        if not visited[i] and graph[idx][i]:
            dfs(i)

  # 0. 입력 및 초기화
MAX = 1000+10 # 제한 값이 1000이 였는데 여유분으로 10개를 더한 것
N,M = map(int, input().split()) #  띄어쓰기를 기준으로 분리해서 int로 받겠다.
graph = [[False]* MAX for _ in range(MAX)] # 2차원 불리언 배열 생성
visited = [False] * MAX # 재방문 방지를 위한 visited 1차원 배열 생성
answer = 0
  
  # 1. graph에 연결 정보 채우기
for _ in range(M):
    u,v = map(int, input().split())
    graph[u][v] = True
    graph[v][u] = True
  
  # 2. DFS 호출
for i in range(1, N+1):
    # 방문한 적이 없는 경우
    if not visited[i]:
        # dfs함수를 실행하겠다.
        # 결국 dfs함수를 몇번 호출했느냐가 정답
        dfs(i)
        answer += 1 # 누적
  
  # 3. 출력
print(answer)