def solution(sizes):
    max_width = max(max(size) for size in sizes)
    # 가로 길이 중 최댓값
    max_height = max(min(size) for size in sizes)       # 세로 길이 중 최댓값
    answer = max_width * max_height
    return answer
