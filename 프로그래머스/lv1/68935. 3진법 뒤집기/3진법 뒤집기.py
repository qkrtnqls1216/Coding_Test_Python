def solution(n):
    num_3 = ''
    while n>0:
        num_10 = n%3 # 나머지 저장
        num_3 = str(num_10) + num_3 # 나머지를 문자열로서 계속 저장
        n = n // 3 # 몫 저장
    return int(num_3[::-1],3) # 문자열을 뒤집고 3진법을 10진수로 변환