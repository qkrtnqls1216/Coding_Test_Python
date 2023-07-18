def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        divisors = 0  # 약수의 개수를 저장하는 변수
        for j in range(1, i + 1):
            if i % j == 0:
                divisors += 1

        if divisors % 2 == 0:
            answer += i
        else:
            answer -= i

    return answer