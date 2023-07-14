def solution(numbers):
    answer = 0
    for i in range(10): # 0~9까지 반복
        if i not in numbers: # numbers에 i값이 없는 경우
            answer += i
    return answer