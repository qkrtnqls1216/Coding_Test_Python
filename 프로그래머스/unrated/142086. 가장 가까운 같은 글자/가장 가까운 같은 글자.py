def solution(s):
    answer = [] # 결과담을 리스트 초기화
    dic = {} # 딕셔너리 초기화
    for i,c in enumerate(s):
        if c in dic:
            answer.append(i - dic[c]) # 인덱스 차이 추가
        else:
            answer.append(-1)  # 해당 문자가 처음 등장한 경우 -1을 결과 추가
        dic[c] = i  # 딕셔너리에 해당 문자의 인덱스 업데이트
    return answer