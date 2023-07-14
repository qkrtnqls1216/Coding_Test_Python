def solution(a, b):
    answer = 0
    if a <= b:
        for i in range(a,b+1): # a가 b보다 작거나 같을 경우
            answer += i
    else: # a>b 즉, a가 n보다 클 경우
        for i in range(a,b-1,-1):
            answer += i
    return answer