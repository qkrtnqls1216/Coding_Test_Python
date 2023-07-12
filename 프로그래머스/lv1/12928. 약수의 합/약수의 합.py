def solution(n):
    answer = 0 # 약수가 저장될 변수 초기화
    for i in range (1,n+1): # 1~n+1전까지 반복
        if(n%i == 0): # 0이면 리스트의 끝에 추가
            answer += i # 약수 저장
    return answer # 답 반환