def solution(s):
    answer = ''
    new = s.split(' ') # 공백으로 구분
    for i in new: # 공백포함 배열 new만큼 반복
        for j in range(len(i)): # i만큼반복
            if j % 2 == 0: # 짝수
                answer += i[j].upper()
            else:# 홀수
                answer += i[j].lower()
        answer+= ' '
    return answer[0:-1]