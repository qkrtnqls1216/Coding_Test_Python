def solution(x, n):
    answer = [] # 리스트에 저장.
    for i in range(n): # 입력받은 n만큼 반복
        answer.append(x*(i+1)) # 리스트의 끝에 추가
    return answer