def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        divisors = 0  # 약수의 개수를 저장하는 변수
        for j in range(1, i + 1):
            if i % j == 0: # 약수인 경우
                divisors += 1 # 약수저장하는 divisors에 저장

        if divisors % 2 == 0: # 약수의 개수가 짝수인 경우
            answer += i 
        else: # 약수의 개수가 홀수인 경우
            answer -= i

    return answer