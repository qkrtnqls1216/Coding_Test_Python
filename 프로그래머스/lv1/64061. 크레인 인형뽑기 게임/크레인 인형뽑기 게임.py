from collections import deque

def solution(board, moves):
    moves = deque(moves)
    buckets = []  # 뽑힌 인형 쌓을 배열
    cnt = 0

    while moves:
        move = moves.popleft()  # 배열의 첫번째 원소제거하여 move에 저장

        for i in range(len(board)):
            doll = board[i][move - 1]  # 현재 뽑힌 인형
            if doll != 0:
                board[i][move - 1] = 0  # 0으로 채움
                if buckets and buckets[-1] == doll:  # buckets에 원소가 존재할 때 buckets의 최상단 원소와 현재뽑힌 인형 doll이 동일할 경우
                    buckets.pop()  # buckets에 있는 원소 제거. 이때 buckets[-1] == doll을 했을때의 원소는 buckets에 쌓기 전이므로 하나만 제거해주면 된다.
                    cnt += 2
                else:  # 아직 buckets에 아무것도 없거나 최상단원소와 인형이 동일하지 않은 경우
                    buckets.append(doll)
                break
    return cnt
