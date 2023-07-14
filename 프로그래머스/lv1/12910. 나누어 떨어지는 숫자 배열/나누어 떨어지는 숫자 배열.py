def solution(arr, divisor):
    answer = []
    for i in arr: # 나누어떨어지는 것만을 저장하기 위해 배열을 반복
        if i % divisor == 0: # 나누어떨어지면 
            answer.append(i) # 배열의 끝에 추가
    if len(answer) == 0:
        return [-1] # answer의 길이가 0이면 -1을 반환
    else:
        return sorted(answer) # answer을 정렬해서 반환