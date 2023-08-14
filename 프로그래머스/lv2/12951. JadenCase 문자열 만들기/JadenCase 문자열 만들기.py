def solution(s):
    answer = []
    s = s.split(' ') # 문자열을 공백을 기준으로 분리
    for i in range(len(s)):
        s[i] = s[i].capitalize()
    answer = ' '.join(s)
    return ''.join(answer)
# 내장함수 capitalize 사용 시 첫 문자가 알파벳일 경우 대문자로하고 이후문자는 자동으로 소문자
# 첫 문자가 알파벳이 아니면 그대로 반환