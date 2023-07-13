import math

def solution(n):
    x=int(math.sqrt(n)) # 주의: math.sqrt 함수는 실수(float) 값을 반환
    if (n == (x**2)):
        answer = (x+1) ** 2
    else:
        answer = -1
    return answer


# n은 양수
# n=x의 제곱이어야 한다. n=x**2
