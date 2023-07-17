def solution(arr):
    if len(arr) > 1: # 배열이 1이 아닌경우
        min_1 = min(arr) # 가장 작은값 저장
        arr.remove(min_1) # 가장 작은값 제거
        answer = arr # 수정된 arr을 answer에 할당
    else: # 배열이 0인경우
        answer = [-1] # 배열을 -1로 채우기 
    return answer