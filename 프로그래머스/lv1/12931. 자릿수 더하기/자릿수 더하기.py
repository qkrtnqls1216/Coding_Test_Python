def solution(N):
    # 자연수 N을 문자열로 변환
    str_1 = str(N)
    
    # 각 자릿수의 합을 저장하기 위해 answer 변수 초기화
    answer = 0

    # 문자열 반복
    for i in str_1:
        # 다시 숫자로 변경하고 sum에 더하기
        answer += int(i)
    return answer

# 문제해석: 숫자열을 문자열로 변환한 후 다시 숫자로 변환하여 더한다.