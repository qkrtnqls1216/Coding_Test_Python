def solution(a, b, n):
    answer = 0
    while n >= a:
        # 현재 가지고 있는 빈 병으로 교환 가능한 콜라의 최대 개수
        temp = (n // a) * b
        # 새로 받은 콜라를 누적
        answer += temp
        # 현재 가지고 있는 빈 병 중, 새로 받은 콜라로 교환되지 않은 빈 병 개수 업데이트
        n = n % a + temp
        
    return answer