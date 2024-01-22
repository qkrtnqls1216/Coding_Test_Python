def solution(k, m, score):
    answer = 0
    # 내림차순으로 정렬
    sorted_list = sorted(score, reverse=True)
    sorted_list
    
    # 리스트를 사과박스에 들어가는 수 만큼씩 여러개 리스트를 분할, 지정개수 이하는 버림
    result = [sorted_list[i * m : (i + 1) * m] for i in range((len(sorted_list) + m - 1) // m) if len(sorted_list[i * m : (i + 1) * m]) == m]
    result

    # 최대이익 계산
    for i in result:
        answer += min(i) * m
    return answer
