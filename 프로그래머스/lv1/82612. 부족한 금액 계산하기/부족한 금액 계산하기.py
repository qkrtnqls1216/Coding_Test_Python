def solution(price, money, count):
    total = price * (count * (count+1)//2) # 총 비용 계산
    if money >= total: # 돈이 있는 경우
        return 0
    else: # 돈이 부족한 경우
        return total - money