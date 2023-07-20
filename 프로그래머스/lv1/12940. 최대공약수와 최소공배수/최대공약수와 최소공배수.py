import math

def solution(n, m):
    answer = []
    max_1 = math.gcd(n,m) # 최대공약수 구하기
    min_1  = n*m // max_1 # 최소공배수 구하기
    answer.append(max_1) # 배열에 추가
    answer.append(min_1)
    return answer