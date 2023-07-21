def solution(d, budget):
    d.sort()  # 부서별 신청 금액을 오름차순으로 정렬
    answer = 0
    for i in range(len(d)): # 부서별 예산신청금액 배열만큼 반복
        if budget >= d[i]: # 보유한 예산이 신청금액보다 많은 경우
            budget -= d[i] # 신청금액만큼 예산 감소
            answer += 1 # 지원한 부서 count
        else: # 예산없는 경우
            break
    return answer