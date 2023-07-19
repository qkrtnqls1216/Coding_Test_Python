def solution(s):
    answer = True
    if len(s)== 4 or len(s)== 6: # s의 길이가 4 또는 6일 경우
        if s.isdigit(): # isdigit(): 문자열이 모두 숫자로 구성되어 있는지 확인하는 함수사용
            # 숫자로 구성되어있는 경우
            answer = True
            return answer
        else: # 길이는 4 또는 6이지만 문자가 섞여있는 경우
            answer = False
            return  answer
    else: # s의길이가 4또는 6이 아닌 경우
        answer = False
        return answer
            