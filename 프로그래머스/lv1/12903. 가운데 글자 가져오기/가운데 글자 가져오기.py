def solution(s):
    lenght = len(s) # s의 길이 저장
    if lenght % 2 == 1: # 홀수일 경우
        answer = s[lenght//2] # 가운데글자를 저장
    else:
        answer = s[lenght//2 - 1:lenght//2+1] # 가운데 글자중 첫번째글자:가운데글자중 두번째글자
    return answer

# 하드코딩
# def solution(s):
#     if len(s) % 2 == 1:
#         answer = s[2:3]
#     else:
#         answer = s[1:3]
#     return answer