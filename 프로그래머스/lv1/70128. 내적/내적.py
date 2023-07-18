def solution(a, b):
    answer = 0
    for i in range(len(a)): # a와 b의 길이가 동일
            answer += a[i]*b[i] # a와b 내적
    return answer