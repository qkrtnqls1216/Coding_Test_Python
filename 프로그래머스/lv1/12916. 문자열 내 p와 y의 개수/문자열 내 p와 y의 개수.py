def solution(s):
    s = s.lower() # 소문자로 통일하기 위해 문자열을 소문자로 변환
    p_len = s.count('p') # p 길이 저장
    y_len = s.count('y') # y 길이 저장
    
    if p_len == y_len: # 길이가 같으면 True
        return True
    elif p_len != y_len: # 길이가 다르면 False
        return  False
    else: # 이외에는 True => 문제의 경우 p,y가 하나도없는 경우가 이 경우에 속한다.
        return True