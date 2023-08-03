def solution(food):
    answer = '' # 왼쪽에서 먹는 선수를 위한 배치
    reverse = '' # 오른쪽에서 먹는 선수를 위한 배치
    for i in range(len(food)):
        if food[i] % 2 == 0:
            answer += str(i) * (food[i]//2)
        else:
            answer += str(i) * (food[i]//2)
    answer += str(0) # 물
    for i in range(len(food)):
        if food[i] % 2 == 0:
            reverse += str(i) * (food[i]//2)
        else:
            reverse += str(i) * (food[i]//2)
    reverse = reverse[::-1]
    answer = answer + reverse
    return answer
