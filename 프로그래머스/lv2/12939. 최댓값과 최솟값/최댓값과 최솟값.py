def solution(s):
    s = s.split(' ') # 공백기준으로 분리
    s = list(map(int,s))
    a,b = min(s),max(s)
    answer = ("%d %d"%(a,b))
    return answer