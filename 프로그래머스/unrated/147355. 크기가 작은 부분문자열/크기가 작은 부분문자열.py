def solution(t, p):
    cnt = 0
    for char in range(len(t)-len(p)+1): # t에서 길이가 p와 같은 부분 문자열을 구하기 위한 인덱스 범위 계산
        answer = t[char:char+len(p)] # p길이 만큼의 값을 배열에 저장
        if answer <= p: # p보다 answer의 값이 작거나 같을 경우
            cnt +=1 # 횟수 증가
    return cnt