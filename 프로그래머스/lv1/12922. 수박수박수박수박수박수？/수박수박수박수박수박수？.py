def solution(n):
    answer = ""
    for i in range(n): # 정수n의 길이 만큼 반복
        if i%2 == 0: # 짝수일 경우 "수" 저장
            answer += "수"
        else:# 홀수일 경우 "박" 저장
            answer += "박"
    return answer # for문이 끝난 뒤 최종 answer값 반환