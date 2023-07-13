def solution(n):
    str_1 = str(n) # sorted사용위해 문자열로 변환
    sort_1 = sorted(str_1,reverse=True)
    answer = int(''.join(sort_1))
    return answer